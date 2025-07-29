# The Value of Art

The value of art é um aplicativo que prevê valor para pinturas baseadas apenas em sua imagem. No aplicativo, você pode fazer o upload da imagem de uma obra de arte e receber uma estimativa do valor da obra¹. O acesso ao aplicativo pode ser feito através do link: 

https://thevalueofart.streamlit.com

![appimage](https://github.com/eudansou/the_value_of_art/blob/master/images/appimage.jpg)

Para além de um aplicativo, o projeto também é o primero passo para entender se é possível, através de Deep Learning, perceber padrões - que passariam desapercebidos - nas imagens que influenciam o valor da obra.

## O modelo e suas métricas. (Como funciona)

O aplicativo (codado utilizando streamlit) está conectado através de uma API (FastAPI) a um modelo CNN (Convolutional Neural Network) treinado numa base dados de 2000 imagens. Obtivemos um MALE (Mean Absolute Logaritmic Error) de 0.21, uma redução de 73% do modelo média. (que prevê apenas o valor médio do dataset para qualquer obra). A métrica MALE foi escolhida pois foi a que se mostrou mais eficiente ao lidar com outliers. Após aplicarmos o logaritmo aos valores do dataset, observamos uma distribuição bem próxima da normal.

## A base de dados

A base de dados é composta por 2000 imagens e algumas outras features de possível importância (estilo, material, dimensões, autor). A base de dados foi obtida através de um web scrapping da galeria Saatchi Art. O código para o scrapping pode ser encontrado no arquivo scraping.py. 

## Modelos Alternativos e Feature Engineering

Dentre os arquivos é possível ainda encontrar notebooks onde se encontram Modelos de Regressão efetuados a partir das outras features da base de dados. Através dos notebook percebe-se que não há - supreendentemente - grande impacto dos materiais e estilo no preço das obras. Através desta análises foi encontrada uma correlação de aproximadamente 0,55 entre a área dos quadros e seus valores. Ela não foi utilizada no cálculo do modelo atual empregado na API - porém é uma feature a ser levada em consideração em futuras continuações do projeto. 

Além disso, também se tentou avaliar a imagem através de features construídas (contraste, composição, textura, etc). Não foram obtidos grandes insights por este caminho, porém é um caminho a se manter em aberto para futuros próximos passos. Junto a especialistas na área, é possível que features mais relevantes possam ser construídas.

## Equipe e Contato

O projeto foi realizado por [Bia Ramalho](https://github.com/Biarsl), [Carolina Gallindo](https://github.com/carolgallin), [Danilo Alexandre](https://github.com/eudansou), [Felipe Moniz](https://github.com/FelipeMoniz), como parte do projeto de conclusão do Batch #1887 do bootcamp de Data Science e AI.

#### Notas
¹ Entendemos que outros fatores tais quais a relevância do autor, área e outros também são significativos no valor da obra. Leve em consideração que a obra já passou por alguma triagem envolvendo curadores e galeristas. 

## English Version

"The value of art" is an application that predicts the value of paintings based solely on their image. In the app, you can upload an image of an artwork and receive an estimated value for the piece¹. The application can be accessed via the following link:

https://thevalueofart.streamlit.com

Beyond being an application, this project is also the first step in understanding whether it is possible, through Deep Learning, to perceive patterns — which might otherwise go unnoticed — in images that influence the value of an artwork.

## The Model and its Metrics (How it works)
The application (coded using Streamlit) is connected via FastAPI to a CNN (Convolutional Neural Network) model trained on a dataset of 2000 images. We achieved an MALE score (Mean Absolute Logarithmic Error) of 0.21, a 73% reduction compared to the baseline model (which predicts only the average value of the dataset for any artwork). The MALE metric was chosen as it proved to be the most effective in handling outliers. After applying the logarithm to the dataset values, we observed a distribution very close to normal.

## The Dataset
The dataset consists of 2000 images and some other features of potential importance (style, material, dimensions, author). The data was obtained by web scraping the Saatchi Art gallery. The code for the scraping can be found in the scraping.py file.

## Alternative Models and Feature Engineering
Among the project files, you can also find notebooks containing Regression Models built using the other features from the dataset. Through these notebooks, it becomes apparent that, surprisingly, materials and style do not have a significant impact on the price of the artworks. This analysis revealed a correlation of approximately 0.55 between the area of the paintings and their values. This was not used in the calculation of the current model deployed in the API; however, it is a feature to be considered in future continuations of the project.

Furthermore, an attempt was made to evaluate the images through engineered features (contrast, composition, texture, etc.). No significant insights were gained from this approach, but it remains an open path for future steps. With the help of experts in the field, it may be possible to engineer more relevant features.

## Team and Contact
This project was carried out by Bia Ramalho, Carolina Gallindo, Danilo Alexandre, and Felipe Moniz as part of the final project for Batch #1887 of the Data Science and AI bootcamp.

### Notes
¹ We understand that other factors, such as the author's relevance, the artwork's area, and others, are also significant in determining its value. Please consider that the artwork has already undergone some form of screening by curators and gallerists.
