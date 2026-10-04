---
id: software.devops.tranche10.000938
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
fontes: ["https://raw.githubusercontent.com/getsops/sops/main/README.rst", "https://getsops.io/docs/usage/common-operations/", "https://getsops.io/docs/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SOPS: criptografia de arquivos binários e injeção segura em processos em memória (sops exec-env e sops exec-file)

## Em uma frase
Além de arquivos estruturados, o SOPS criptografa arquivos **binários** arbitrários (armazenando o payload Base64 cifrado sob `tree['data']` em JSON) e executa processos filhos injetando segredos diretamente em variáveis de ambiente (**`sops exec-env`**) ou arquivos temporários FIFO/tmpfs (**`sops exec-file`**) sem deixar texto claro no disco.

## Por que importa
Um erro operacional comum ao usar o SOPS localmente ou em CI é rodar `sops decrypt secrets.enc.env > .env` no disco para executar um comando (`terraform apply` ou `kubectl apply`) e esquecer de apagar o arquivo `.env` descriptografado (ou o script falhar antes do `rm .env`, deixando segredos expostos no runner ou sendo comitados por acidente).

## Como funciona
(1) **Arquivos binários**: conforme explica a seção `Encrypting binary files` de `Common operations`, ao criptografar um binário (certificado `.p12`, arquivo `.tar.gz` ou imagem), o SOPS lê os bytes brutos, cifra-os, armazena o resultado em Base64 sob a chave `data` de um documento JSON e o restaura exatamente com o mesmo hash SHA-512 no `sops decrypt`; (2) **`sops exec-env <arquivo.enc.yaml> '<comando>'`**: descriptografa as chaves de primeiro nível do arquivo em memória, injeta-as como variáveis de ambiente exclusivamente no processo filho `<comando>` e encerra; e (3) **`sops exec-file <arquivo.enc> '<comando> {}'`**: disponibiliza o conteúdo descriptografado em um arquivo temporário em memória/FIFO (`{}`) que é destruído automaticamente assim que `<comando>` termina.

## Exemplo
```bash
# Executar o Terraform ou uma aplicação injetando os segredos descriptografados apenas na memória do processo filho
sops exec-env secrets.enc.yaml 'terraform plan'
sops exec-file kubeconfig.enc.yaml 'kubectl --kubeconfig {} get nodes'
```

## Limites e trade-offs
Conforme observa a documentação oficial na seção `Encrypting binary files`, devido à codificação Base64 dos bytes cifrados dentro do envelope JSON, o arquivo binário criptografado pelo SOPS será cerca de 33% maior em disco do que o arquivo binário original em texto claro.

## Como verificar
Execute `sops exec-env secrets.enc.yaml 'env'` para verificar que as variáveis do arquivo criptografado estão presentes no subprocesso sem que nenhum arquivo descriptografado tenha sido gravado no diretório atual (`ls -la`).

## Conexões
- [[sops-gerenciamento-chaves-updatekeys-rotate-keygroups]] — Veja também: SOPS: rotação da chave de dados (sops rotate), sincronização de receptores (sops updatekeys) e Key Groups (Shamir).
- [[sops-integracao-gitops-flux-argocd-helm-secrets]] — Veja também: SOPS: integração nativa com pipelines GitOps no Kubernetes (Flux kustomize-controller, helm-secrets e KSOPS).
- [[sops-editor-arquivos-criptografados-yaml-json-env-ini]] — Referência cruzada direta com sops-editor-arquivos-criptografados-yaml-json-env-ini.
- [[sops-operacoes-arvore-extract-set-unset-in-place]] — Referência cruzada direta com sops-operacoes-arvore-extract-set-unset-in-place.

## Fontes
- [SOPS GitHub — README.rst & Official Docs Overview (Supported Formats, KMS/age/PGP & Format 1.0 Backward Compatibility)](https://raw.githubusercontent.com/getsops/sops/main/README.rst) — README e página inicial de documentação do SOPS (projeto CNCF Sandbox, MPL-2.0) sobre formatos suportados, provedores KMS/age/PGP e garantia de retrocompatibilidade desde a versão 1.0; consultado em 2026-10-03.
- [SOPS Official Documentation — Common Operations (Encrypt/Decrypt, In-Place, --extract, sops set/unset, Git Diff textconv & --encrypted-regex)](https://getsops.io/docs/usage/common-operations/) — Documentação oficial de operações comuns do SOPS cobrindo edição, criptografia de arquivos binários, --extract, sops set/unset, diffs em texto claro no Git (.gitattributes) e criptografia seletiva com --encrypted-regex e MAC; consultado em 2026-10-03.
- [SOPS Official Documentation — Usage & Key Management Guide](https://getsops.io/docs/) — Guia oficial de uso, identidades e gerenciamento de chaves do SOPS; consultado em 2026-10-03.
