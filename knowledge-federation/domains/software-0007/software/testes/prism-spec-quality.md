---
id: software.testes.tranche16.001040
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
fontes: ["https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking", "https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: a simulação depende da qualidade do contrato

## Em uma frase
Rotas, parâmetros e respostas simuladas derivam diretamente do documento, e imprecisões aparecem como comportamento inesperado do servidor.

## Por que importa
Uma simulação estranha geralmente revela que o contrato está incompleto, ambíguo ou desatualizado, e não que a ferramenta esteja errada.

## Como funciona
Valide o documento com verificador de esquema, mantenha exemplos significativos e trate divergências descobertas na simulação como correções no contrato.

## Exemplo
Uma rota ausente no documento simplesmente não existe na simulação, apontando lacuna de cobertura da especificação.

## Limites e trade-offs
Ferramentas de verificação checam estrutura, mas não julgam se o contrato descreve o comportamento desejado do serviço.

## Como verificar
Remova um campo do contrato e confirme que a simulação deixa de responder esse conteúdo, evidenciando a dependência direta do documento.

## Conexões
- [[prism-generated-errors]] — Veja também: Prism: entender as respostas de violação.
- [[prism-cli-workflow]] — Veja também: Prism: operar a linha de comando.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
