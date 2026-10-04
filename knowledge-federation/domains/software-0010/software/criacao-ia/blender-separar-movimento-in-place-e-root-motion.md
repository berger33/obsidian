---
id: software.criacao_ia.tranche01.000069
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.blender.org/manual/en/latest/animation/actions.html", "https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender: separar movimento in-place e root motion

## Em uma frase

Animação pode codificar deslocamento no root ou manter personagem no lugar para o controlador de gameplay mover o corpo.

## Por que importa

A escolha afeta sincronização entre clip e física, navegação e autoridade de rede.

## Como funciona

Defina a convenção com a engine, modele deslocamento conforme necessário e deixe claro qual componente é dono do movimento.

## Exemplo

Uma corrida in-place deixa o CharacterController mover o NPC; uma animação cinematográfica pode conservar movimento na raiz.

## Limites e trade-offs

Combinar root motion e movimento de código sem coordenação causa velocidade duplicada e dessincronização.

## Como verificar

Compare distância animada com distância do controlador e teste aceleração, parada e correção de colisão.

## Conexões
- [[blender-controlar-multiplas-actions-no-export]] — Blender: controlar múltiplas Actions no export.
- [[blender-revisar-animacao-dentro-do-jogo]] — Blender: revisar animação dentro do jogo.

## Fontes
- [Blender Manual — Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) — Descreve ações e seu uso para organizar dados de animação no Blender. Consulta: 2026-10-04.
- [Blender Manual — glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) — Documenta opções, objetos e animações suportados pela exportação glTF do Blender. Consulta: 2026-10-04.
