---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Como validar codigo gerado por IA"]
---
# Como validar codigo gerado por IA

## Pergunta inicial
Como validar codigo gerado por IA?

## Versão em texto
- **Tem testes** → [[Testes-unitarios]]
- **Sem testes** → [[QA-manual-com-IA]]
- **Mudança crítica** → [[Code-review]]
- **Segurança** → [[Seguranca-web]]

## Diagrama
```mermaid
flowchart TD
    A[Como validar codigo gerado por IA]
    A --> B1[Tem testes]
    B1 --> L1[[Testes-unitarios]]
    A --> B2[Sem testes]
    B2 --> L2[[QA-manual-com-IA]]
    A --> B3[Mudança crítica]
    B3 --> L3[[Code-review]]
    A --> B4[Segurança]
    B4 --> L4[[Seguranca-web]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
