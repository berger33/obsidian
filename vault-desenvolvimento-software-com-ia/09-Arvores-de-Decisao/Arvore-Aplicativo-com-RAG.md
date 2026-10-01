---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Aplicativo com RAG"]
---
# Aplicativo com RAG

## Pergunta inicial
Aplicativo com RAG?

## Versão em texto
- **Docs estáveis** → [[RAG-para-desenvolvimento]]
- **Busca semântica** → [[Vector-database]]
- **Dados sensíveis** → [[Privacidade-com-agentes]]
- **Atualizações frequentes** → [[Data-pipeline]]

## Diagrama
```mermaid
flowchart TD
    A[Aplicativo com RAG]
    A --> B1[Docs estáveis]
    B1 --> L1[[RAG-para-desenvolvimento]]
    A --> B2[Busca semântica]
    B2 --> L2[[Vector-database]]
    A --> B3[Dados sensíveis]
    B3 --> L3[[Privacidade-com-agentes]]
    A --> B4[Atualizações frequentes]
    B4 --> L4[[Data-pipeline]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
