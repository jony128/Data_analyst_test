O filtro foi montado em python com opções de variaveis que podem ser alteradas facilmente dependendo da metrica que iremos utilizar

O codigo gera um DataFrame que calcula porcentagem e adiciona o valor a coluna "pgt_final"
mostrando também um grafico em python para exibição de valores maiores que 15% de porcentagem 
como todos os clientes do CSV utilizavam a metrica de > 100 e < 200 o padrão foi sempre 15%
porém caso algum cliente saisse dessa metrica poderiamos adicionar e alterar a porcentagem com somente uma linha de codigo

o plot grafico também iria ser alterado caso houvesse clientes com diferentes margens e poderiamos ter uma noção de quais são nossas margens de clientes

O código tem muita espaço para melhora e aplicação de clean code porém com as condições atuais dessa forma é mais pratico e simples