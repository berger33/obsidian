---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Refatorar com IA"]
---
# Refatorar com IA

## Pergunta inicial
Refatorar com IA?

## Versão em texto
- **Tem testes** → [[Refatoracao]]
- **Sem testes** → [[Testes-unitarios]]
- **Muitos arquivos** → [[Diff-review]]
- **Legado** → [[Divida-tecnica]]

## Diagrama
```mermaid
flowchart TD
    A[Refatorar com IA]
    A --> B1[Tem testes]
    B1 --> L1[[Refatoracao]]
    A --> B2[Sem testes]
    B2 --> L2[[Testes-unitarios]]
    A --> B3[Muitos arquivos]
    B3 --> L3[[Diff-review]]
    A --> B4[Legado]
    B4 --> L4[[Divida-tecnica]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
