---
id: software.criacao_ia.tranche01.000019
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

# Responses API: tratar falhas e repetição

## Em uma frase

Erros de rede, limites de taxa e respostas incompletas precisam de estados de aplicação diferentes de uma geração bem-sucedida.

## Por que importa

Confundir falha técnica com texto vazio pode apagar trabalho do usuário ou fazer o cliente apresentar uma conclusão inexistente.

## Como funciona

Mapeie códigos e estados documentados, mostre uma mensagem segura e escolha repetição apenas para operações que possam ser repetidas com segurança.

## Exemplo

Uma prévia de fala pode tentar novamente após timeout, mas uma ação que salva compra ou consome crédito exige controle de duplicidade.

## Limites e trade-offs

Políticas de retry agressivas ampliam latência e podem piorar congestionamento ou duplicar efeitos laterais.

## Como verificar

Simule timeout, limite de taxa e erro permanente; verifique limites de tentativas, observabilidade e consistência da interface.

## Conexões
- [[responses-api-isolar-conteudo-nao-confiavel]] — Responses API: isolar conteúdo não confiável.
- [[responses-api-avaliar-geracao-com-exemplos]] — Responses API: avaliar geração com exemplos.

## Fontes
- [OpenAI API — Text generation](https://platform.openai.com/docs/guides/text) — Guia oficial de geração de texto, instruções, entradas e saídas pela Responses API. Consulta: 2026-10-04.
- [OpenAI API — Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering) — Recomendações oficiais para compor instruções, contexto e avaliação de prompts. Consulta: 2026-10-04.
