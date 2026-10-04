---
id: software.testes.tranche16.001051
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
fontes: ["https://hurl.dev/docs/manual.html", "https://github.com/Orange-OpenSource/hurl"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: executar vários arquivos em paralelo

## Em uma frase
O modo de teste recebe arquivos ou diretórios, executa em paralelo com número controlado de tarefas e apresenta resumo por arquivo.

## Por que importa
Tratar cada arquivo como unidade independente permite escalar a verificação e isolar falhas por caso.

## Como funciona
Nomeie os arquivos de forma descritiva, agrupe por recurso ou jornada e use o modo de teste com paralelismo compatível com o ambiente.

## Exemplo
Um diretório de verificação pode conter arquivos por recurso, executados em paralelo com resumo final destacando os que falharam.

## Limites e trade-offs
Os arquivos não compartilham sessão no modo de teste, então dados que dependem de ordem precisam estar no mesmo arquivo ou em preparação comum.

## Como verificar
Execute o diretório completo e confirme que o resumo lista todos os arquivos com resultado próprio e total coerente.

## Conexões
- [[hurl-options-block]] — Veja também: Hurl: configurar comportamento por entrada.
- [[hurl-session-scope]] — Veja também: Hurl: entender o escopo da sessão.

## Fontes
- [Hurl — Manual (CLI)](https://hurl.dev/docs/manual.html) — modo de teste, paralelismo, repetição, relatórios e códigos de saída; consultado em 2026-10-03.
- [Hurl — repositório oficial](https://github.com/Orange-OpenSource/hurl) — visão geral do projeto, exemplos e documentação complementar; consultado em 2026-10-03.
