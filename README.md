# The Value of Art

The value of art é um aplicativo que prevê valor para pinturas baseadas apenas em sua imagem. No aplicativo, você pode fazer o upload da imagem de uma obra de arte e receber uma estimativa do valor da obra¹. O acesso ao aplicativo pode ser feito através do link: 

https://thevalueofart.streamlit.com

Para além de um aplicativo, o projeto também é o primero passo para entender se é possível, através de Deep Learning, perceber padrões - que passariam desapercebidos - nas imagens que influenciam o valor da obra.

## O modelo e suas métricas. (Como funciona)

O aplicativo (codado utilizando streamlit) está conectado através de uma API (FastAPI) a um modelo CNN (Convolutional Neural Network) treinado numa base dados de 2000 imagens. Obtivemos um MALE (Mean Absolute Logaritmic Error) de 0.21, uma redução de 73% do modelo média. (que prevê apenas o valor médio do dataset para qualquer obra). A métrica MALE foi escolhida pois foi a que se mostrou mais eficiente ao lidar com outliers. Após aplicarmos o logaritmo aos valores do dataset, observamos uma distribuição bem próxima da normal.

## A base de dados

A base de dados é composta por 2000 imagens e algumas outras features de possível importância (estilo, material, dimensões, autor). A base de dados foi obtida através de um web scrapping da galeria Saatchi Art. O código para o scrapping pode ser encontrado no arquivo scrapping.py. 

## Modelos Alternativos e Feature Engineering

Dentre os arquivos é possível ainda encontrar notebooks onde se encontram Modelos de Regressão efetuados a partir das outras features da base de dados. Através dos notebook percebe-se que não há - supreendentemente - grande impacto dos materiais e estilo no preço das obras. Através desta análises foi encontrada uma correlação de aproximadamente 0,55 entre a área dos quadros e seus valores. Ela não foi utilizada no cálculo do modelo atual empregado na API - porém é uma feature a ser levada em consideração em futuras continuações do projeto. 

Além disso, também se tentou avaliar a imagem através de features construídas (contraste, composição, textura, etc). Não foram obtidos grandes insights por este caminho, porém é um caminho a se manter em aberto para futuros próximos passos. Junto a especialistas na área, é possível que features mais relevantes possam ser construídas.

## Equipe

O projeto foi realizado por Bia Ramalho, Carolina Gallindo, Danilo Alexandre e Felipe Moniz, como parte do projeto de conclusão do Batch #1887 do bootcamp de Data Science e AI.

#### Notas
¹ Entendemos que outros fatores tais quais a relevância do autor, área e outros também são significativos no valor da obra. Leve em consideração que a obra já passou por alguma triagem envolvendo curadores e galeristas.  
