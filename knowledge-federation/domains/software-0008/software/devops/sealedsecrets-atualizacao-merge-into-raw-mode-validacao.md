---
id: software.devops.tranche10.000926
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
fontes: ["https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md", "https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md", "https://github.com/bitnami-labs/sealed-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Bitnami Sealed Secrets: adição de itens sem conhecer chaves antigas (--merge-into), modo --raw e validação (--validate)

## Em uma frase
O `kubeseal` permite adicionar ou atualizar uma única chave dentro de um `SealedSecret` existente sem ter acesso aos valores originais das demais chaves usando **`--merge-into`**, criptografar strings isoladas com **`--raw`** e validar integridade com **`--validate`**.

## Por que importa
Em uma equipe com 10 desenvolvedores, o arquivo `app-sealed-secret.yaml` no Git já possui 8 chaves criptografadas (cujos valores em texto claro o desenvolvedor atual não conhece nem precisa conhecer). Quando ele precisa adicionar uma 9ª chave (`NEW_API_KEY`), ele não pode recriar o `Secret` inteiro do zero — ele precisa mesclar apenas a nova chave cifrada no `SealedSecret` existente.

## Como funciona
Conforme documenta a seção `Usage` (`Update existing secrets`, `Raw mode` e `Validate a Sealed Secret`) do README oficial: (1) **`--merge-into`**: ao rodar `echo -n bar | kubectl create secret generic mysecret --dry-run=client --from-file=foo=/dev/stdin -o yaml | kubeseal --merge-into mysealedsecret.yaml`, o `kubeseal` cifra apenas a chave `foo` (respeitando o mesmo nome/namespace/escopo) e atualiza in-place o arquivo `mysealedsecret.yaml` preservando todas as outras chaves criptografadas intactas; (2) **`--raw`**: cifra apenas um valor individual no `stdout` (para colar manualmente em um arquivo YAML/Helm values) sem gerar o manifesto `SealedSecret` inteiro; e (3) **`--validate`**: pede ao controlador para verificar se um `SealedSecret` é válido e descriptografável sem aplicá-lo no cluster.

## Exemplo
```bash
# Adicionar ou atualizar apenas a chave 'nova-chave' dentro de um arquivo mysealedsecret.yaml já existente no Git
echo -n "novo-valor-secreto" \
  | kubectl create secret generic mysecret --dry-run=client --from-file=nova-chave=/dev/stdin -o yaml \
  | kubeseal -o yaml --merge-into mysealedsecret.yaml
```

## Limites e trade-offs
Ao usar `echo` no terminal para passar o valor de um segredo via pipe (`/dev/stdin`) para o `kubectl create secret` ou `kubeseal --raw`, passe sempre a flag **`echo -n`** (sem quebra de linha final `\n`), pois o `echo` padrão adiciona um caractere `\n` invisível ao final da senha que causará falhas sutis de autenticação na aplicação quando o `Secret` for descriptografado!

## Como verificar
Após executar `kubeseal --merge-into mysealedsecret.yaml`, rode `git diff mysealedsecret.yaml` para confirmar que apenas a linha `nova-chave` foi adicionada ou alterada em `spec.encryptedData`.

## Conexões
- [[sealedsecrets-rotacao-chaves-sealing-key-renewal-re-encrypt]] — Veja também: Bitnami Sealed Secrets: renovação periódica de chaves de selamento (30 dias), rotação de segredos e re-encryption.
- [[sealedsecrets-criptografia-hibrida-aes-gcm-rsa-oaep-detalhes]] — Veja também: Bitnami Sealed Secrets: funcionamento interno da criptografia híbrida (AES-256-GCM + RSA-OAep-SHA256).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide]] — Referência cruzada direta com sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide.
- [[sealedsecrets-templates-metadados-ownerreferences-tipos-secret]] — Referência cruzada direta com sealedsecrets-templates-metadados-ownerreferences-tipos-secret.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
