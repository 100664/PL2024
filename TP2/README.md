# Conversor de MD para HTML

## Autor

Martim José Amaro Redondo, A100664

## Funcionalidades implementadas

1. Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto" por "<h1>Exemplo</h1>", ou "<h2>Exemplo</h2>" ou "<h3>Exemplo</h3>", respetivamente.

2. Bold: pedaços de texto entre "**":
      - In: Este é um **exemplo** ...
      - Out: Este é um <b>exemplo</b> ...
3. Itálico: pedaços de texto entre "*":
      - In: Este é um *exemplo* ...
      - Out: Este é um <i>exemplo</i> ...
4. Lista numerada:
      - In:
        1. Primeiro item
        2. Segundo item
        3. Terceiro item
      - Out:
      <ol>
      <li>Primeiro item</li>
      <li>Segundo item</li>
      <li>Terceiro item</li>
      </ol>
5. Link: [texto](endereço URL)
      - In: Como pode ser consultado em [página da UC](http://www.uc.pt)
      - Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
6. Imagem: ![texto alternativo](path para a imagem)
      - In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
      - Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...

