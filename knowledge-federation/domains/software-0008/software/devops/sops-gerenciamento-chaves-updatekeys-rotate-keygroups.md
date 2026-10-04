---
id: software.devops.tranche10.000937
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
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/usage/", "https://getsops.io/docs/usage/common-operations/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS: rotação da chave de dados (sops rotate), sincronização de receptores (sops updatekeys) e Key Groups (Shamir)

## Em uma frase
O SOPS separa a sincronização da lista de chaves mestras autorizadas a abrir um arquivo (**`sops updatekeys`**) da rotação efetiva da chave de criptografia de dados e recifragem de todos os valores (**`sops rotate`**), suportando ainda **Key Groups** com divisão de segredo de Shamir (`shamir_threshold`).

## Por que importa
Quando um novo membro entra na equipe (ou sai da empresa) e você atualiza as chaves públicas no `.sops.yaml`, os 50 arquivos `.enc.yaml` que já estavam comitados no Git continuam cifrados apenas para as chaves antigas até que você sincronize seus cabeçalhos (`updatekeys`) e rotacione a chave de dados (`rotate`).

## Como funciona
(1) **`sops updatekeys arquivo.enc.yaml`**: compara as chaves mestras atualmente presentes no bloco `sops:` do arquivo contra as regras atuais do `.sops.yaml`, mostra um diff das chaves que serão adicionadas ou removidas e cifra/remove a DEK para os receptores afetados; (2) **`sops rotate -i arquivo.enc.yaml`**: gera uma **nova Data Encryption Key (DEK)** aleatória e recifra todos os valores do arquivo com a nova DEK (podendo adicionar/remover chaves mestras ao mesmo tempo com `--add-kms`, `--rm-pgp`, etc.); e (3) **Key Groups e `shamir_threshold`**: permite dividir a DEK usando Shamir's Secret Sharing entre múltiplos grupos de chaves (ex.: exigir simultaneamente 1 chave do AWS KMS **e** 1 chave PGP de um administrador para conseguir descriptografar).

## Exemplo
```bash
# Sincronizar os receptores de um arquivo criptografado após editar o .sops.yaml e rotacionar a chave de dados (DEK)
sops updatekeys -y clusters/prod/secrets.enc.yaml
sops rotate -i clusters/prod/secrets.enc.yaml
```

## Limites e trade-offs
Quando um desenvolvedor com acesso à chave privada sai da organização, apenas remover a chave dele via `sops updatekeys` (e mesmo rodar `sops rotate`) impede que ele abra futuras versões do arquivo, mas ele ainda poderia descriptografar commits históricos do Git usando a chave antiga; portanto, ao revogar o acesso de alguém, além de rodar `sops updatekeys` e `sops rotate`, **rotacione os valores das credenciais reais** nos serviços de destino.

## Como verificar
Execute `sops rotate -i secrets.enc.yaml` e verifique com `git diff` que todas as strings `ENC[AES256_GCM,data:...]` e o timestamp `lastmodified` foram recifrados com uma nova DEK.

## Conexões
- [[sops-provedores-identidades-kms-age-pgp-vault]] — Veja também: SOPS: identidades e provedores de chaves mestras (age, PGP, AWS KMS, GCP KMS, Azure Key Vault e HashiCorp Vault).
- [[sops-arquivos-binarios-exec-env-exec-file-processos]] — Veja também: SOPS: criptografia de arquivos binários e injeção segura em processos em memória (sops exec-env e sops exec-file).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-regras-criacao-arquivo-sops-yaml-path-regex]] — Referência cruzada direta com sops-regras-criacao-arquivo-sops-yaml-path-regex.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/usage/common-operations/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
