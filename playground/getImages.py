from PIL import Image
from sentence_transformers import SentenceTransformer, util
import os
from PIL import Image
import torch

def get_Images(k, keywordpargraph=None, keyimage=None):
    key_image_vector = None
    print('Starting building models')
    text_model = SentenceTransformer('clip-ViT-B-32-multilingual-v1')
    image_model = SentenceTransformer('clip-ViT-B-32')
    print('Building models finished')
    if keyimage:
        print(keyimage)
        keyImage_RGB_array = []
        keyImage_RGB_array.append(Image.open(keyimage).convert('RGB'))
        print('Starting encoding keyimage')
        key_image_vector = image_model.encode(keyImage_RGB_array)
        print('Encoding keyimage finished')
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
    print('Start encoding image tensors')
    image_directory = 'images'
    image_tensors = load_images_from_directory(image_directory)
    image_vectors = image_model.encode(image_tensors)
    print('Encoding image tensors finished')
    # def find_keyword_index(keyword=None, key_image_vector=None):
    #     if keyword is None and key_image_vector is None:
    #         raise ValueError("At least one of 'keyword' or 'key_image_vector' must be provided.")

    #     if keyword is not None:
    #         text_vec = text_model.encode([keyword])

    #     image_sims = []
    #     max_sim_index = [float('-inf'), 0]

    #     for i in range(image_vectors.shape[0]):
    #         sim_keyword = 0
    #         sim_keyimage = 0
    #         count = 0

    #         if keyword is not None:
    #             sim_keyword = util.cos_sim(text_vec, image_vectors[i])
    #             count += 1

    #         if key_image_vector is not None:
    #             sim_keyimage = util.cos_sim(key_image_vector, image_vectors[i])
    #             count += 1

    #         # Calculate the average similarity
    #         sim_avg = (sim_keyword + sim_keyimage) / count

    #         if sim_avg > max_sim_index[0]:
    #             max_sim_index = [sim_avg, i]

    #         image_sims.append([sim_avg, i])

    #     return max_sim_index[1]
    def find_k_most_matched_indexes(k, output_path='images',source_path ='images',keyword=None, key_image_vector=None):
        if keyword is None and key_image_vector is None:
            raise ValueError("At least one of 'keyword' or 'key_image_vector' must be provided.")

        if keyword is not None:
            print('Starting encoding keywords')
            text_vec = text_model.encode([keyword])
            print('Encoding keywords finished')

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
        image_sims.sort(reverse=True)
        k_most_matched_indexes = image_sims[:k]
        count = 1
        final_sims = []
        imageNames = []
        for sim, index in k_most_matched_indexes:
            if not os.path.exists('static/images'):
                os.makedirs('static/images')
            
            str_max_sim_index = str(index).zfill(4)
            image_path = source_path +  '/' + str_max_sim_index +'.png'
            img = Image.open(image_path)
            newImageName = os.path.join(output_path, str(count).zfill(4) + '.png')
            imageNames.append(newImageName)
            img.save(os.path.join('static', newImageName))
            img.close()
            count += 1
            final_sims.append(sim.item())
        print(final_sims)
        print(imageNames)

        return final_sims, imageNames
    if keywordpargraph and keyimage:
        return find_k_most_matched_indexes(k, keyword=keywordpargraph, key_image_vector=key_image_vector)
    elif keywordpargraph:
        return find_k_most_matched_indexes(k, keyword=keywordpargraph)
    else:
        return find_k_most_matched_indexes(k, key_image_vector=key_image_vector)
    # # max_sim_index = find_keyword_index(keywordpargraph)
    # max_sim_index = k_most_matched_index[0][1]
    # str_max_sim_index = str(max_sim_index + 1).zfill(4)
    # image_path = 'images/' + str_max_sim_index +'.png'
    # img = Image.open(image_path)
    # if not os.path.exists("result"):
    #   os.makedirs("result")
    # img.save('result/finalImage.png')
    # img.close()

