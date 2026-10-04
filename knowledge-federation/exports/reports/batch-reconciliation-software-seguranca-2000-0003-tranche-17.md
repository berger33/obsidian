# Reconciliação estrutural — lote `software-seguranca-2000-0003`, tranche 17 (IDs `1601–1700`)

Reconciliação dos 100 arquivos Markdown substantivos da tranche 17: o lote avança para **1700/2.000 (85,00%)** e o total global para **5740/1.000.000 (0,5740%)** (49 aprovações humanas históricas + 5691 revisões por IA registradas).

## Inventário da tranche

- IDs efetivamente materializados: `1601–1700`; 100 arquivos Markdown distintos, sem IDs reservados ou placeholders.
- Gate de conteúdo e revisão factual: 100/100 notas; revisão por IA registrada no relatório [`ai-review-software-seguranca-2000-0003-tranche-17.md`](ai-review-software-seguranca-2000-0003-tranche-17.md); nenhum campo de revisão humana foi alterado.
- Arquivos ativos após esta tranche: 5840; incluem 100 notas legadas pendentes, que continuam fora da contagem.
- Registro de revisão: linhas 5641–5740 da fila; MOC, manifesto e índices globais atualizados.
- Status do lote: `in_progress`; notas restantes no lote: 300.

## Famílias temáticas

- 1601–1610: **Trivy** — scanner de vulnerabilidades, segredos, configurações e licenças para imagens, sistemas de arquivos e infraestrutura como código.
- 1611–1620: **Syft** — gerador de SBOM que cataloga pacotes de imagens, diretórios, arquivos de imagem e outros alvos suportados.
- 1621–1630: **Grype** — scanner de vulnerabilidades para imagens, sistemas de arquivos e SBOMs, incluindo pacotes de sistema operacional e linguagens.
- 1631–1640: **Sigstore Cosign** — ferramenta de assinatura, verificação e atestação de artefatos OCI e blobs com suporte a chaves e identidade OIDC.
- 1641–1650: **Open Policy Agent (OPA)** — motor de políticas que avalia dados estruturados com Rego e pode ser integrado a serviços e pipelines.
- 1651–1660: **Kyverno** — motor de políticas Kubernetes que valida, modifica, gera e verifica configurações e imagens em recursos.
- 1661–1670: **Falco** — motor de detecção em runtime que avalia streams de eventos contra regras de comportamento anômalo.
- 1671–1680: **Checkov** — analisador de configuração para infraestrutura como código e artefatos cloud-native com checks embutidos e personalizados.
- 1681–1690: **kube-bench** — ferramenta que audita a configuração de nós e componentes Kubernetes segundo checks de benchmarks CIS.
- 1691–1700: **OWASP ASVS** — padrão aberto de requisitos para verificar controles técnicos de segurança em aplicações web.

## Evidências e verificações

1. Relatório factual por IA: `knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md`; 100 decisões registradas, referências primárias e limites por nota.
2. Relatório de qualidade do lote: `knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md`; auditado após o acréscimo das notas.
3. Gate de palavras, frontmatter, seções, fontes HTTPS, links wiki, títulos/IDs e sentenças repetidas verificado antes da atualização global.
4. `python3 -m unittest discover -s knowledge-federation/tests -v`: **12/12 testes passaram** em 0,020 s (2026-10-04).
5. `python3 knowledge-federation/scripts/audit_note_quality.py --path knowledge-federation/domains --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz`: **5.840 arquivos avaliados, 5.740 notas válidas, 49 humanas, 5.691 IA e 100 pendências**. O arquivo de auditoria registra ainda 1.000.000 de registros virtuais/template e 8.000 materializados no ledger; nenhum deles foi contado como nota substantiva.

Esta reconciliação é editorial e não usa catálogo virtual, arquivo vazio, link, nem identificador reservado como progresso.
