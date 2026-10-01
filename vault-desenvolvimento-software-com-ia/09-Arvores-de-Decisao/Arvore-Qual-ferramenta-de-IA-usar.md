---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Qual ferramenta de IA usar"]
---
# Qual ferramenta de IA usar

## Pergunta inicial
Qual ferramenta de IA usar?

## Versão em texto
- **IDE o dia todo** → [[Cursor]]
- **Terminal e repo** → [[Claude-Code]]
- **App do zero** → [[Lovable]]
- **Revisão e segurança** → [[CodeRabbit]]

## Diagrama
```mermaid
flowchart TD
    A[Qual ferramenta de IA usar]
    A --> B1[IDE o dia todo]
    B1 --> L1[[Cursor]]
    A --> B2[Terminal e repo]
    B2 --> L2[[Claude-Code]]
    A --> B3[App do zero]
    B3 --> L3[[Lovable]]
    A --> B4[Revisão e segurança]
    B4 --> L4[[CodeRabbit]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
