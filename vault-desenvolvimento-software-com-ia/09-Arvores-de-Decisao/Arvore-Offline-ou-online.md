---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Offline ou online"]
---
# Offline ou online

## Pergunta inicial
Offline ou online?

## Versão em texto
- **Primeiro jogo** → [[Single-player-offline]]
- **Competitivo** → [[Online-competitivo]]
- **Coop simples** → [[Online-cooperativo]]
- **MMO** → [[MMO-para-solo-dev]]

## Diagrama
```mermaid
flowchart TD
    A[Offline ou online]
    A --> B1[Primeiro jogo]
    B1 --> L1[[Single-player-offline]]
    A --> B2[Competitivo]
    B2 --> L2[[Online-competitivo]]
    A --> B3[Coop simples]
    B3 --> L3[[Online-cooperativo]]
    A --> B4[MMO]
    B4 --> L4[[MMO-para-solo-dev]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
