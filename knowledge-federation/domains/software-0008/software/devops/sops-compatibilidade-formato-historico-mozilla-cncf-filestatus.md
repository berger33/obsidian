---
id: software.devops.tranche10.000940
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/", "https://getsops.io/docs/usage/common-operations/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS: governança CNCF Sandbox, garantia de retrocompatibilidade do formato 1.0+ e comando sops filestatus

## Em uma frase
Conforme documenta a página inicial de `getsops.io/docs/`, o SOPS mantém garantia estrita de retrocompatibilidade de formato de arquivo desde a versão **1.0** e oferece utilitários como `sops filestatus` para verificar programaticamente se um arquivo já está criptografado antes de um commit.

## Por que importa
Arquivos criptografados costumam permanecer armazenados em repositórios Git corporativos e backups de longo prazo por muitos anos; saber que novas versões do SOPS (v3.x) preservam compatibilidade com o formato introduzido na v1.0 e validar via pre-commit hook que nenhum arquivo de segredo ficou em texto claro previne vazamentos acidentais.

## Como funciona
(1) **Histórico e Governança**: lançado originalmente na Mozilla em 2015 (por Adrian Utrilla e Julien Vehent, inspirado em `hiera-eyaml`, `credstash`, `sneaker` e `password store`) e doado à **CNCF como projeto Sandbox em 2023** sob licença **MPL-2.0**, o SOPS garante compatibilidade do formato de arquivo em toda a série; e (2) **Verificação de status (`sops filestatus`)**: executar **`sops filestatus <arquivo>`** inspeciona o arquivo e retorna um objeto JSON `{"encrypted": true}` ou `{"encrypted": false}` sem precisar das chaves privadas de descriptografia, permitindo que hooks de `pre-commit` ou jobs de CI bloqueiem instantaneamente qualquer Pull Request que tente comitar um arquivo de segredos com `"encrypted": false`.

## Exemplo
```bash
# Verificar em um script de CI ou pre-commit hook se um arquivo de segredos está devidamente criptografado com SOPS
sops filestatus clusters/prod/secrets.enc.yaml
```

## Limites e trade-offs
O comando `sops filestatus` verifica se a estrutura de metadados `sops` está presente no arquivo (retornando `"encrypted": true`), mas não verifica a validade criptográfica do MAC nem se todos os campos sensíveis foram cobertos por `encrypted_regex` sem descriptografar; em pipelines de CI com acesso a uma chave de leitura de validação ou usando `pre-commit` hooks oficiais do SOPS, combine a checagem de `filestatus` com regras estritas no `.sops.yaml`.

## Como verificar
Execute `sops filestatus secrets.enc.yaml` em um arquivo criptografado e em um arquivo YAML comum e confirme que a saída JSON reporta `{"encrypted":true}` e `{"encrypted":false}` respectivamente.

## Conexões
- [[sops-integracao-gitops-flux-argocd-helm-secrets]] — Veja também: SOPS: integração nativa com pipelines GitOps no Kubernetes (Flux kustomize-controller, helm-secrets e KSOPS).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-regras-criacao-arquivo-sops-yaml-path-regex]] — Referência cruzada direta com sops-regras-criacao-arquivo-sops-yaml-path-regex.
- [[sops-gerenciamento-chaves-updatekeys-rotate-keygroups]] — Referência cruzada direta com sops-gerenciamento-chaves-updatekeys-rotate-keygroups.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/usage/common-operations/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
