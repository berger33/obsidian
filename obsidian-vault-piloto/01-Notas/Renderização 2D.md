---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, renderizacao, performance]
conexoes_chave: ["[[Sprites e atlases]]", "[[Tilemaps]]", "[[Performance em jogos 2D]]", "[[Câmera 2D]]"]
---

# Renderização 2D

#jogos2d #renderizacao #performance

## Resumo
Transforma estado visual em imagem, respeitando ordem, camadas, materiais e custo de desenho.

## Pergunta que esta nota responde
Que ordem visual e que custo de renderização a cena exige?

## Definição operacional
Renderização 2D lida com sprites, tilemaps, sorting layers, parallax, iluminação 2D, shaders e efeitos. A clareza visual é tão importante quanto a eficiência.

## Quando usar
- Ao definir estilo visual.
- Quando elementos aparecem na ordem errada.
- Quando efeitos visuais degradam FPS.

## Sinais de boa aplicação
- Camadas visuais têm convenção.
- Efeitos têm orçamento.
- A cena comunica prioridade sem poluição.

## Conexões
- [[Sprites e atlases]]
- [[Tilemaps]]
- [[Performance em jogos 2D]]
- [[Câmera 2D]]
- [[Pipeline de assets]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
