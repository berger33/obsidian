---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Deploy de MVP"]
---
# Deploy de MVP

## Pergunta inicial
Deploy de MVP?

## Versão em texto
- **Frontend** → [[Hospedagem-Vercel]]
- **Full stack** → [[Hospedagem-Railway]]
- **Backend worker** → [[Docker]]
- **Cloud flexível** → [[AWS-para-apps]]

## Diagrama
```mermaid
flowchart TD
    A[Deploy de MVP]
    A --> B1[Frontend]
    B1 --> L1[[Hospedagem-Vercel]]
    A --> B2[Full stack]
    B2 --> L2[[Hospedagem-Railway]]
    A --> B3[Backend worker]
    B3 --> L3[[Docker]]
    A --> B4[Cloud flexível]
    B4 --> L4[[AWS-para-apps]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
