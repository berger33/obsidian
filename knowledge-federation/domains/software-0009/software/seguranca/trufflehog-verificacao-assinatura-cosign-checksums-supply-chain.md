---
id: software.seguranca.tranche01.000016
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

# TruffleHog Supply Chain Security: verificação criptográfica de binários e `checksums.txt` com Sigstore `cosign verify-blob`

## Em uma frase
Conforme documentado no README oficial do TruffleHog, todos os artefatos de release têm seus hashes SHA-256 gravados em `trufflehog_{version}_checksums.txt`, e esse arquivo de checksums é assinado criptograficamente usando **Sigstore Cosign** (*keyless signing* vinculado ao GitHub Actions OIDC).

## Por que importa
Como um scanner de segredos recebe acesso de leitura a todo o código-fonte, variáveis de CI e tokens da organização, baixar um binário de scanner adulterado em uma pipeline de CI seria catastrófico para a segurança da cadeia de suprimentos.

## Como funciona
Você pode validar a autenticidade da release manualmente com `cosign verify-blob` e `sha256sum -c`, ou passar a flag **`-v`** diretamente para o script oficial de instalação (`install.sh | sh -s -- -v -b /usr/local/bin`), que executa a verificação Cosign automaticamente antes de instalar o binário.

## Exemplo
```bash
# Verificando a assinatura Cosign do arquivo de checksums antes de validar o binário do TruffleHog:
cosign verify-blob trufflehog_3.82.0_checksums.txt \
  --certificate trufflehog_3.82.0_checksums.txt.pem \
  --signature trufflehog_3.82.0_checksums.txt.sig \
  --certificate-identity-regexp 'https://github\.com/trufflesecurity/trufflehog/\.github/workflows/.+' \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"

sha256sum --ignore-missing -c trufflehog_3.82.0_checksums.txt
```

## Limites e trade-offs
Para usar a flag `-v` no script `scripts/install.sh`, o binário `cosign` já deve estar instalado no `PATH` da máquina ou imagem de runner.

## Como verificar
Execute o comando `cosign verify-blob` acima e confirme a mensagem `Verified OK` antes de instalar em runners corporativos.

## Conexões
- [[trufflehog-ci-cd-github-actions-gitlab-ci-since-commit-branch-fail]] — Veja também: TruffleHog em Pipelines CI/CD: varredura diferencial com `--since-commit`, `--branch` e código de saída `--fail` (`183`).
- [[trufflehog-custom-regex-detectors-webhook-verification-config]] — Veja também: TruffleHog Custom Detectors (`--config`): criação de detectores Regex customizados com verificação via servidor Webhook.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
