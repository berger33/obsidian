# Reconciliação estrutural — lote `software-seguranca-2000-0003`, tranche 20 (IDs `1901–2000`)

Reconciliação dos 100 arquivos Markdown substantivos da tranche 20: o lote avança para **2000/2.000 (100,00%)** e o total global para **6040/1.000.000 (0,6040%)** (49 aprovações humanas históricas + 5991 revisões por IA registradas).

## Inventário da tranche

- IDs efetivamente materializados: `1901–2000`; 100 arquivos Markdown distintos, sem IDs reservados ou placeholders.
- Gate de conteúdo e revisão factual: 100/100 notas; revisão por IA registrada no relatório [`ai-review-software-seguranca-2000-0003-tranche-20.md`](ai-review-software-seguranca-2000-0003-tranche-20.md); nenhum campo de revisão humana foi alterado.
- Arquivos ativos após esta tranche: 6140; incluem 100 notas legadas pendentes, que continuam fora da contagem.
- Registro de revisão: linhas 5941–6040 da fila; MOC, manifesto e índices globais atualizados.
- Status do lote: `complete`; notas restantes no lote: 0.

## Famílias temáticas

- 1901–1910: **SLSA** — framework para descrever níveis de garantia da supply chain de software e a proveniência de builds.
- 1911–1920: **The Update Framework (TUF)** — framework de metadados assinados para distribuir atualizações resistentes a rollback, freeze e comprometimento de chaves.
- 1921–1930: **OpenVEX** — formato aberto e compacto para comunicar status de vulnerabilidades em produtos e componentes.
- 1931–1940: **CycloneDX Generator (cdxgen)** — gerador de Software Bill of Materials do ecossistema CycloneDX para código, dependências, imagens e outros alvos.
- 1941–1950: **GitHub Artifact Attestations** — recurso do GitHub para gerar e verificar attestations de build e identidade de origem para artefatos e imagens.
- 1951–1960: **Docker Scout** — serviço de análise de imagens e SBOMs Docker que identifica vulnerabilidades e oferece recomendações de políticas.
- 1961–1970: **Chainguard Images e Wolfi** — ecossistema de imagens de container mínimas baseadas em Wolfi, com metadados de pacote e evidências de build.
- 1971–1980: **RustSec cargo-audit** — ferramenta RustSec que compara dependências bloqueadas em Cargo.lock com a base de advisories de Rust.
- 1981–1990: **OpenSSF Best Practices Badge** — programa de autoavaliação pública de práticas para projetos FLOSS com critérios organizados por níveis.
- 1991–2000: **Reproducible Builds** — prática de produzir bit-a-bit o mesmo artefato a partir do mesmo código-fonte e instruções de build.

## Evidências e verificações

1. Relatório factual por IA: `knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md`; 100 decisões registradas, referências primárias e limites por nota.
2. Relatório de qualidade do lote: `knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md`; auditado após o acréscimo das notas.
3. Gate de palavras, frontmatter, seções, fontes HTTPS, links wiki, títulos/IDs e sentenças repetidas verificado antes da atualização global.
4. Verificações pré-push: `python3 -m unittest discover -s knowledge-federation/tests -v` — 12/12 passaram; auditoria global — 6.140 arquivos, 6.040 candidatas, 6.040 notas válidas (49 humanas + 5.991 IA) e 100 pendências legadas fora da contagem. O ledger conserva 1.000.000 de registros virtuais com marcadores de template (8.000 materializados), sem contabilizá-los como progresso.

Esta reconciliação é editorial e não usa catálogo virtual, arquivo vazio, link, nem identificador reservado como progresso.
