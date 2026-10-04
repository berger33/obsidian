---
id: software.criacao_ia.tranche01.000017
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://platform.openai.com/docs/guides/text", "https://platform.openai.com/docs/guides/prompt-engineering"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Responses API: criar um prompt versionável

## Em uma frase

Guardar prompts como configuração versionada permite reproduzir mudanças de comportamento e relacioná-las a releases do aplicativo.

## Por que importa

Editar instruções diretamente em produção dificulta investigar regressões ou comparar resultados entre versões.

## Como funciona

Separe texto de instrução do código de transporte, atribua uma versão e vincule alterações a testes e revisão de produto.

## Exemplo

Uma atualização do prompt de NPCs pode ser testada em conjunto contra personagens, idiomas e cenas que eram aceitos pela versão anterior.

## Limites e trade-offs

A versão do prompt não fixa a versão do modelo, ferramentas ou dados e não garante determinismo da resposta.

## Como verificar

Registre as combinações relevantes e rode uma suíte de regressão sempre que mudar prompt, modelo ou opções de geração.

## Conexões
- [[responses-api-limitar-o-tamanho-da-saida]] — Responses API: limitar o tamanho da saída.
- [[responses-api-isolar-conteudo-nao-confiavel]] — Responses API: isolar conteúdo não confiável.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
