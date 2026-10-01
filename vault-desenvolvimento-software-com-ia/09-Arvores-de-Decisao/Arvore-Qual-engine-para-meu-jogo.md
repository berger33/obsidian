---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Qual engine para meu jogo"]
---
# Qual engine para meu jogo

## Pergunta inicial
Qual engine para meu jogo?

## Versão em texto
- **2D open source** → [[Godot]]
- **2D comercial rápido** → [[GameMaker]]
- **3D high-end** → [[Unreal-Engine]]
- **Web HTML5** → [[Phaser]]

## Diagrama
```mermaid
flowchart TD
    A[Qual engine para meu jogo]
    A --> B1[2D open source]
    B1 --> L1[[Godot]]
    A --> B2[2D comercial rápido]
    B2 --> L2[[GameMaker]]
    A --> B3[3D high-end]
    B3 --> L3[[Unreal-Engine]]
    A --> B4[Web HTML5]
    B4 --> L4[[Phaser]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
