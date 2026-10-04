# Reconciliação estrutural — lote `software-seguranca-2000-0003`, tranche 18 (IDs `1701–1800`)

Reconciliação dos 100 arquivos Markdown substantivos da tranche 18: o lote avança para **1800/2.000 (90,00%)** e o total global para **5840/1.000.000 (0,5840%)** (49 aprovações humanas históricas + 5791 revisões por IA registradas).

## Inventário da tranche

- IDs efetivamente materializados: `1701–1800`; 100 arquivos Markdown distintos, sem IDs reservados ou placeholders.
- Gate de conteúdo e revisão factual: 100/100 notas; revisão por IA registrada no relatório [`ai-review-software-seguranca-2000-0003-tranche-18.md`](ai-review-software-seguranca-2000-0003-tranche-18.md); nenhum campo de revisão humana foi alterado.
- Arquivos ativos após esta tranche: 5940; incluem 100 notas legadas pendentes, que continuam fora da contagem.
- Registro de revisão: linhas 5741–5840 da fila; MOC, manifesto e índices globais atualizados.
- Status do lote: `in_progress`; notas restantes no lote: 200.

## Famílias temáticas

- 1701–1710: **Semgrep** — analisador estático com regras YAML para detectar padrões de segurança, desempenho e correção em código-fonte.
- 1711–1720: **SonarQube Server** — plataforma de análise de código integrada a scanners, perfis de qualidade e quality gates para equipes de desenvolvimento.
- 1721–1730: **Snyk CLI** — interface de linha de comando para análise de dependências, código, imagens de containers, IaC e segredos.
- 1731–1740: **Kubescape** — scanner de segurança Kubernetes que avalia clusters, manifests e charts contra frameworks e controles publicados.
- 1741–1750: **KubeLinter** — analisador estático para YAML Kubernetes, charts Helm e manifests Kustomize com checks padrão e configuráveis.
- 1751–1760: **Cilium Tetragon** — sistema eBPF de observabilidade e enforcement de segurança em runtime para processos, arquivos e rede.
- 1761–1770: **Renovate** — bot de atualização de dependências que cria branches e pull requests configuráveis para repositórios de software.
- 1771–1780: **GitHub Dependabot** — serviço do GitHub que informa vulnerabilidades em dependências e pode propor atualizações via pull request.
- 1781–1790: **CycloneDX CLI** — ferramenta de linha de comando para validar, analisar, mesclar, comparar, converter e assinar documentos BOM.
- 1791–1800: **AWS CloudFormation Guard** — ferramenta policy-as-code para validar dados JSON ou YAML com regras declarativas antes da implantação.

## Evidências e verificações

1. Relatório factual por IA: `knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md`; 100 decisões registradas, referências primárias e limites por nota.
2. Relatório de qualidade do lote: `knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md`; auditado após o acréscimo das notas.
3. Gate de palavras, frontmatter, seções, fontes HTTPS, links wiki, títulos/IDs e sentenças repetidas verificado antes da atualização global.
4. Verificações pré-push: `python3 -m unittest discover -s knowledge-federation/tests -v` — 12/12 passaram; auditoria global — 5.940 arquivos, 5.840 candidatas, 5.840 notas válidas (49 humanas + 5.791 IA) e 100 pendências legadas fora da contagem. O ledger conserva 1.000.000 de registros virtuais com marcadores de template (8.000 materializados), sem contabilizá-los como progresso.

Esta reconciliação é editorial e não usa catálogo virtual, arquivo vazio, link, nem identificador reservado como progresso.
