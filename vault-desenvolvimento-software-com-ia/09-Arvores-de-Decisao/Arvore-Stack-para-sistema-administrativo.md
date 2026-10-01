---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Stack para sistema administrativo"]
---
# Stack para sistema administrativo

## Pergunta inicial
Stack para sistema administrativo?

## Versão em texto
- **CRUD simples** → [[Dashboard-administrativo]]
- **SaaS multi tenant** → [[Sistema-multi-tenant]]
- **Dados sensíveis** → [[Autenticacao]]
- **Time pequeno** → [[Monolito-modular]]

## Diagrama
```mermaid
flowchart TD
    A[Stack para sistema administrativo]
    A --> B1[CRUD simples]
    B1 --> L1[[Dashboard-administrativo]]
    A --> B2[SaaS multi tenant]
    B2 --> L2[[Sistema-multi-tenant]]
    A --> B3[Dados sensíveis]
    B3 --> L3[[Autenticacao]]
    A --> B4[Time pequeno]
    B4 --> L4[[Monolito-modular]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
