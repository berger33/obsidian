---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["2D ou 3D"]
---
# 2D ou 3D

## Pergunta inicial
2D ou 3D?

## Versão em texto
- **Escopo solo** → [[Jogo-2D]]
- **Visual high fidelity** → [[Jogo-3D]]
- **Aprender fundamentos** → [[Godot]]
- **Web/mobile leve** → [[Phaser]]

## Diagrama
```mermaid
flowchart TD
    A[2D ou 3D]
    A --> B1[Escopo solo]
    B1 --> L1[[Jogo-2D]]
    A --> B2[Visual high fidelity]
    B2 --> L2[[Jogo-3D]]
    A --> B3[Aprender fundamentos]
    B3 --> L3[[Godot]]
    A --> B4[Web/mobile leve]
    B4 --> L4[[Phaser]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
