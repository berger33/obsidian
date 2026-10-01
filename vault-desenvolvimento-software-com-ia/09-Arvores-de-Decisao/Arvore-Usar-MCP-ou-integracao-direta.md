---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Usar MCP ou integracao direta"]
---
# Usar MCP ou integracao direta

## Pergunta inicial
Usar MCP ou integracao direta?

## Versão em texto
- **Ferramenta reutilizável** → [[MCP-Model-Context-Protocol]]
- **Integração simples** → [[Tool-use]]
- **Segurança crítica** → [[Seguranca-de-MCP-servers]]
- **Ecossistema agentes** → [[Clientes-MCP]]

## Diagrama
```mermaid
flowchart TD
    A[Usar MCP ou integracao direta]
    A --> B1[Ferramenta reutilizável]
    B1 --> L1[[MCP-Model-Context-Protocol]]
    A --> B2[Integração simples]
    B2 --> L2[[Tool-use]]
    A --> B3[Segurança crítica]
    B3 --> L3[[Seguranca-de-MCP-servers]]
    A --> B4[Ecossistema agentes]
    B4 --> L4[[Clientes-MCP]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
