from PIL import Image
from sentence_transformers import SentenceTransformer, util
import os
from PIL import Image
import torch

def get_Images(keywordpargraph):
    text_model = SentenceTransformer('clip-ViT-B-32-multilingual-v1')
    image_model = SentenceTransformer('clip-ViT-B-32')

    def load_images_from_directory(directory):
        image_tensors = []

        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                # Load the image and convert it to RGB mode
                image = Image.open(os.path.join(directory, file)).convert('RGB')
                
                # # Convert the image to a PyTorch tensor and normalize the pixel values
                # image_tensor = torch.tensor(image).permute(2, 0, 1) / 255.0

                # # Append the image tensor to the list
                image_tensors.append(image)

        return image_tensors

    image_directory = 'images'
    image_tensors = load_images_from_directory(image_directory)
    image_vectors = image_model.encode(image_tensors)

    def find_keyword_index(keyword=None, key_image_vector=None):
        if keyword is None and key_image_vector is None:
            raise ValueError("At least one of 'keyword' or 'key_image_vector' must be provided.")

        if keyword is not None:
            text_vec = text_model.encode([keyword])

        image_sims = []
        max_sim_index = [float('-inf'), 0]

        for i in range(image_vectors.shape[0]):
            sim_keyword = 0
            sim_keyimage = 0
            count = 0

            if keyword is not None:
                sim_keyword = util.cos_sim(text_vec, image_vectors[i])
                count += 1

            if key_image_vector is not None:
                sim_keyimage = util.cos_sim(key_image_vector, image_vectors[i])
                count += 1

            # Calculate the average similarity
            sim_avg = (sim_keyword + sim_keyimage) / count

            if sim_avg > max_sim_index[0]:
                max_sim_index = [sim_avg, i]

            image_sims.append([sim_avg, i])

        return max_sim_index[1]

    max_sim_index = find_keyword_index(keywordpargraph)
    str_max_sim_index = str(max_sim_index + 1).zfill(4)
    image_path = 'images/' + str_max_sim_index +'.png'
    img = Image.open(image_path)
    if not os.path.exists("result"):
      os.makedirs("result")
    img.save('result/finalImage.png')
    img.close()
