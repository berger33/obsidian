---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Escolher multiplayer"]
---
# Escolher multiplayer

## Pergunta inicial
Escolher multiplayer?

## Versão em texto
- **Local** → [[Multiplayer-local]]
- **Casual online** → [[Online-cooperativo]]
- **Competitivo** → [[Rollback-netcode]]
- **MMO** → [[MMORPG-viabilidade]]

## Diagrama
```mermaid
flowchart TD
    A[Escolher multiplayer]
    A --> B1[Local]
    B1 --> L1[[Multiplayer-local]]
    A --> B2[Casual online]
    B2 --> L2[[Online-cooperativo]]
    A --> B3[Competitivo]
    B3 --> L3[[Rollback-netcode]]
    A --> B4[MMO]
    B4 --> L4[[MMORPG-viabilidade]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
