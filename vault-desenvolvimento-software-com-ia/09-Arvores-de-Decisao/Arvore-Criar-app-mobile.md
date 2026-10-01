---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Criar app mobile"]
---
# Criar app mobile

## Pergunta inicial
Criar app mobile?

## Versão em texto
- **Nativo** → [[Mobile-Android-nativo]]
- **Uma base** → [[Flutter]]
- **Web suficiente** → [[PWA-mobile]]
- **Performance UI** → [[React-Native]]

## Diagrama
```mermaid
flowchart TD
    A[Criar app mobile]
    A --> B1[Nativo]
    B1 --> L1[[Mobile-Android-nativo]]
    A --> B2[Uma base]
    B2 --> L2[[Flutter]]
    A --> B3[Web suficiente]
    B3 --> L3[[PWA-mobile]]
    A --> B4[Performance UI]
    B4 --> L4[[React-Native]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
