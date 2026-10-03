---
id: software.seguranca.tranche01.000013
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md", "https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md", "https://github.com/trufflesecurity/trufflehog"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TruffleHog Políticas de Verificação: controle de `--results=verified,unknown,unverified` e modo offline `--no-verification`

## Em uma frase
O TruffleHog permite controlar com precisão a política de verificação de credenciais por meio das flags **`--results`** (`verified`, `unverified`, `unknown`, `filtered_unverified`) e **`--no-verification`** (que desativa qualquer chamada de rede externa aos provedores das credenciais).

## Por que importa
Em ambientes altamente restritos ou durante auditorias onde você não deseja que o scanner realize chamadas HTTP para APIs externas com os tokens encontrados, é essencial saber quando usar verificação ativa versus modo puramente offline.

## Como funciona
Os estados de resultado têm semânticas precisas: 1) **`verified`**: o detector contatou o provedor (ex.: `sts:GetCallerIdentity` na AWS) e confirmou que a credencial está ativa; 2) **`unverified`**: o formato corresponde ao detector, mas o provedor rejeitou a credencial como revogada/inválida; e 3) **`unknown`**: houve erro transitório de rede/timeout durante a tentativa de verificação.

## Exemplo
```bash
# Em CI/CD, falhando o build (exit code 183) caso encontre segredos verificados ou com falha de verificação (unknown):
trufflehog git file://. --since-commit main --results=verified,unknown --fail

# Em ambiente air-gapped, desabilitando chamadas de rede de verificação externa:
trufflehog filesystem ./src --no-verification --json
```

## Limites e trade-offs
Em pipelines de CI, recomenda-se usar **`--results=verified,unknown --fail`** para que uma falha temporária de DNS/rede ao verificar uma credencial real (`unknown`) não permita que o segredo passe silenciosamente.

## Como verificar
Verifique no output JSON (`--json`) o campo `"Verified": true/false` de cada resultado.

## Conexões
- [[trufflehog-fontes-varredura-git-github-gitlab-s3-gcs-docker-filesystem]] — Veja também: TruffleHog Fontes de Varredura: inspeção nativa de `git`, `github`, `gitlab`, `s3`, `gcs`, `docker` (camadas OCI) e `filesystem`.
- [[trufflehog-analise-profunda-credenciais-analyze-iam-permissions]] — Veja também: TruffleHog Credential Analysis (`trufflehog analyze`): mapeamento de identidade, recursos acessíveis e permissões de chaves vazadas.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
