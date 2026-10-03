---
id: software.testes.tranche15.000874
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/branch.html", "https://coverage.readthedocs.io/en/latest/excluding.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: usar pragma no branch para desvios estruturalmente parciais

## Em uma frase
Branch coverage acompanha transições possíveis entre linhas e pode marcar uma saída não executada como partial branch mesmo quando as statements visíveis parecem cobertas.

## Por que importa
Em loops que intencionalmente terminam por `break`, expressões geradoras consumidas parcialmente ou caminhos que não podem ocorrer pelo contrato do programa, a análise estática pode não inferir que uma alternativa é inalcançável.

## Como funciona
`# pragma: no branch` sinaliza uma exceção localizada, enquanto `# pragma: no cover` exclui código de forma mais ampla.

## Exemplo
Adicione `# pragma: no branch` apenas à linha de controle cujo destino alternativo é intencionalmente inalcançável e documente no código qual invariante garante isso.

## Limites e trade-offs
Pragma reduz o que o relatório considera exigível; usá-lo para esconder um ramo possível transforma um indicador em aparência e não melhora a suíte.

## Como verificar
Inspecione os destinos ausentes em HTML ou texto, remova o pragma temporariamente e confirme que o relatório acusa exatamente a alternativa prevista.

## Conexões
- [[coverage-py-subprocessos-e-instrumentacao]] — Veja também: coverage.py: propagar medição a subprocessos de forma configurada.
- [[coverage-py-exclusao-de-codigo-afeta-o-total]] — Veja também: coverage.py: revisar como exclusões alteram statements e branches reportados.

## Fontes
- [Coverage.py 7.16.2 — Branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html) — destinos parciais, linhas ausentes e pragma no branch; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Excluding code](https://coverage.readthedocs.io/en/latest/excluding.html) — exclusões de linhas/blocos e efeito sobre branch coverage; consultado em 2026-10-02.
