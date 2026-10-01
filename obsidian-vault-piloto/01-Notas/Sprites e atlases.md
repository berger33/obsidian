---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, arte, performance]
conexoes_chave: ["[[Pipeline de assets]]", "[[Renderização 2D]]", "[[Animação 2D]]", "[[Performance em jogos 2D]]"]
---

# Sprites e atlases

#jogos2d #arte #performance

## Resumo
Sprites são imagens 2D; atlases agrupam sprites para reduzir trocas de textura e organizar assets.

## Pergunta que esta nota responde
Como preparar arte para renderizar bem sem destruir o fluxo dos artistas?

## Definição operacional
Um sprite representa um elemento visual 2D. Um atlas reúne múltiplos sprites em uma textura maior, otimizando renderização e empacotamento. A decisão afeta memória, draw calls, animação e pipeline.

## Quando usar
- Quando há muitos elementos visuais pequenos.
- Quando performance cai por trocas de textura.
- Quando a equipe precisa padronizar exportação de assets.

## Sinais de boa aplicação
- Nomes e pivôs são consistentes.
- Atlas não mistura assets com ciclos de mudança muito diferentes.
- A compactação não causa artefatos visuais.

## Conexões
- [[Pipeline de assets]]
- [[Renderização 2D]]
- [[Animação 2D]]
- [[Performance em jogos 2D]]
- [[Câmera 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
