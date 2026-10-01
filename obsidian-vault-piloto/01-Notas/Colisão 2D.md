---
tipo: ficha
status: semente
camada: jogos2d
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, fisica, gameplay]
conexoes_chave: ["[[Game loop]]", "[[Física 2D]]", "[[Tilemaps]]", "[[IA de inimigos 2D]]"]
---

# Colisão 2D

#jogos2d #fisica #gameplay

## Resumo
Detecta e resolve interações espaciais entre personagens, objetos, tiles e gatilhos.

## Pergunta que esta nota responde
O jogo precisa de colisão física realista ou de regras de gameplay previsíveis?

## Definição operacional
Colisão 2D envolve formas, layers, máscaras, detecção, resolução e eventos. Em muitos jogos, sensação e previsibilidade valem mais que realismo físico.

## Quando usar
- Ao implementar movimento, dano, plataformas e pickups.
- Ao separar hitboxes, hurtboxes e triggers.
- Quando bugs de atravessar parede aparecem.

## Sinais de boa aplicação
- Camadas de colisão têm nomes claros.
- Hitbox e visual não precisam ser idênticos.
- O comportamento é previsível em bordas e alta velocidade.

## Conexões
- [[Game loop]]
- [[Física 2D]]
- [[Tilemaps]]
- [[IA de inimigos 2D]]
- [[Sistemas determinísticos]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
