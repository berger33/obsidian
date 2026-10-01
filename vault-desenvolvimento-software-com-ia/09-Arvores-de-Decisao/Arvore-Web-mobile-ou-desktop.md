---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Web mobile ou desktop"]
---
# Web mobile ou desktop

## Pergunta inicial
Web mobile ou desktop?

## Versão em texto
- **Distribuição imediata** → [[PWA-Progressive-Web-App]]
- **Loja mobile** → [[Mobile-Android-nativo]]
- **Acesso a sistema local** → [[Desktop-Tauri]]
- **Offline forte** → [[Apps-offline-first]]

## Diagrama
```mermaid
flowchart TD
    A[Web mobile ou desktop]
    A --> B1[Distribuição imediata]
    B1 --> L1[[PWA-Progressive-Web-App]]
    A --> B2[Loja mobile]
    B2 --> L2[[Mobile-Android-nativo]]
    A --> B3[Acesso a sistema local]
    B3 --> L3[[Desktop-Tauri]]
    A --> B4[Offline forte]
    B4 --> L4[[Apps-offline-first]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
