---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, automacao, arte]
conexoes_chave: ["[[Sprites e atlases]]", "[[Tilemaps]]", "[[Renderização 2D]]", "[[CI-CD]]"]
---

# Pipeline de assets

#jogos2d #automacao #arte

## Resumo
Fluxo que leva arte, áudio e dados da criação até o jogo de forma repetível.

## Pergunta que esta nota responde
Como transformar arquivos de produção em assets prontos sem depender de passos manuais frágeis?

## Definição operacional
Pipeline de assets define nomes, formatos, exportação, compressão, validação, importação e versionamento. Em jogos 2D, impacta sprites, atlases, tilemaps, animações, áudio e dados de fases.

## Quando usar
- Quando artistas e programadores perdem tempo com importação manual.
- Quando assets quebram por inconsistência de nomes.
- Quando builds precisam ser reproduzíveis.

## Sinais de boa aplicação
- Convenções são documentadas.
- Validações pegam erros cedo.
- O processo suporta iteração rápida.

## Conexões
- [[Sprites e atlases]]
- [[Tilemaps]]
- [[Renderização 2D]]
- [[CI-CD]]
- [[Registro de decisões arquiteturais]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
