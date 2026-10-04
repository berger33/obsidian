---
id: software.seguranca.tranche01.000015
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

# TruffleHog em Pipelines CI/CD: varredura diferencial com `--since-commit`, `--branch` e código de saída `--fail` (`183`)

## Em uma frase
Para rodar o TruffleHog em pipelines de integração contínua (GitHub Actions, GitLab CI, Jenkins, CircleCI) sem reescanear todo o histórico do repositório a cada push, o subcomando `trufflehog git` oferece as flags **`--since-commit`**, **`--branch`** e **`--fail`** (que retorna o código de saída **`183`** quando resultados são encontrados).

## Por que importa
Se um job de Pull Request escanear desde o commit inicial da empresa, qualquer credencial antiga em outra branch ou commit passado quebraria o PR de um desenvolvedor que alterou apenas um arquivo CSS.

## Como funciona
Passando `--since-commit <base-branch-sha>` e `--branch <head-branch>` com `--fail`, o TruffleHog percorre apenas os commits introduzidos no Pull Request e retorna exit code `183` se encontrar credenciais que atendam ao filtro `--results`, bloqueando o merge.

## Exemplo
```bash
# Varredura diferencial de uma branch em relação à main com falha determinística para CI:
trufflehog git file://. \
  --since-commit origin/main \
  --branch HEAD \
  --results=verified,unknown \
  --fail
```

## Limites e trade-offs
Observe que o TruffleHog exige que o histórico Git no runner de CI possua ao menos os commits entre a base e o HEAD (ex.: `fetch-depth: 0` no `actions/checkout`).

## Como verificar
Confira o código de retorno (`echo $?`) após rodar `trufflehog ... --fail`: `0` significa limpo e `183` significa segredos detectados.

## Conexões
- [[trufflehog-analise-profunda-credenciais-analyze-iam-permissions]] — Veja também: TruffleHog Credential Analysis (`trufflehog analyze`): mapeamento de identidade, recursos acessíveis e permissões de chaves vazadas.
- [[trufflehog-verificacao-assinatura-cosign-checksums-supply-chain]] — Veja também: TruffleHog Supply Chain Security: verificação criptográfica de binários e `checksums.txt` com Sigstore `cosign verify-blob`.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
