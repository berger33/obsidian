---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Qual modelo usar para codigo"]
---
# Qual modelo usar para codigo

## Pergunta inicial
Qual modelo usar para codigo?

## Versão em texto
- **Qualidade máxima** → [[Claude-Opus-para-codigo]]
- **Custo baixo** → [[Gemini-Flash-para-codigo]]
- **Local privado** → [[Llama-para-codigo-local]]
- **Long context** → [[Context-window]]

## Diagrama
```mermaid
flowchart TD
    A[Qual modelo usar para codigo]
    A --> B1[Qualidade máxima]
    B1 --> L1[[Claude-Opus-para-codigo]]
    A --> B2[Custo baixo]
    B2 --> L2[[Gemini-Flash-para-codigo]]
    A --> B3[Local privado]
    B3 --> L3[[Llama-para-codigo-local]]
    A --> B4[Long context]
    B4 --> L4[[Context-window]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
