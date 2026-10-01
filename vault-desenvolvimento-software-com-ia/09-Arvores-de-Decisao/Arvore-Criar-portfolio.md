---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Criar portfolio"]
---
# Criar portfolio

## Pergunta inicial
Criar portfolio?

## Versão em texto
- **Apps úteis** → [[Portfolio-de-orquestrador-IA]]
- **Jogos** → [[Portfolio-de-jogos-pequenos]]
- **Open source** → [[Open-source-como-estrategia]]
- **Case study** → [[Documentacao-tecnica]]

## Diagrama
```mermaid
flowchart TD
    A[Criar portfolio]
    A --> B1[Apps úteis]
    B1 --> L1[[Portfolio-de-orquestrador-IA]]
    A --> B2[Jogos]
    B2 --> L2[[Portfolio-de-jogos-pequenos]]
    A --> B3[Open source]
    B3 --> L3[[Open-source-como-estrategia]]
    A --> B4[Case study]
    B4 --> L4[[Documentacao-tecnica]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
