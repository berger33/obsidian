---
id: software.testes.tranche16.001041
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli", "https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: operar a linha de comando

## Em uma frase
A ferramenta de linha de comando oferece execução do servidor de simulação e do intermediário, com opções de porta, modo estrito e hospedagem do documento a partir de endereço remoto.

## Por que importa
Automatizar a subida da simulação permite incorporá-la a testes de integração e a ambientes de demonstração de forma reproduzível.

## Como funciona
Suba a simulação a partir de arquivo local ou endereço versionado, fixe porta e modo, e encerre o processo ao final da execução automatizada.

## Exemplo
Uma suíte de integração pode iniciar a simulação em segundo plano, aguardar a porta responder e derrubar o processo ao terminar.

## Limites e trade-offs
Documentos buscados de endereço remoto introduzem dependência de rede no teste; versione o arquivo e evite puxar a especificação a cada execução.

## Como verificar
Inicie a simulação, consulte uma rota e confirme no log que o documento carregado é exatamente o arquivo versionado no repositório.

## Conexões
- [[prism-spec-quality]] — Veja também: Prism: a simulação depende da qualidade do contrato.
- [[prism-client-programmatic]] — Veja também: Prism: usar a biblioteca em código de teste.

## Fontes
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
