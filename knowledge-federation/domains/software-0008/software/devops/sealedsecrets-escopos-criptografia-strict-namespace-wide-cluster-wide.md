---
id: software.devops.tranche10.000922
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

# Bitnami Sealed Secrets: os 3 escopos de criptografia (strict, namespace-wide e cluster-wide) contra movimentação não autorizada

## Em uma frase
O Sealed Secrets protege contra a cópia maliciosa de recursos `SealedSecret` entre namespaces ou nomes diferentes vinculando criptograficamente a identidade do segredo em três escopos selecionáveis (`--scope`): **`strict`** (padrão), **`namespace-wide`** e **`cluster-wide`**.

## Por que importa
Se os arquivos `SealedSecret` estão visíveis no Git para todos os desenvolvedores da empresa, mas cada desenvolvedor só tem permissão RBAC para ler `Secret`s no seu próprio namespace `dev-alice`, o que impediria um usuário mal-intencionado de pegar um `SealedSecret` do namespace `production` no Git, mudar `metadata.namespace: dev-alice` no YAML, aplicá-lo no seu namespace e ler o `Secret` descriptografado pelo controlador? A seção `Scopes` do README oficial explica como os escopos impedem exatamente esse ataque.

## Como funciona
Durante o processo de criptografia pelo `kubeseal`, atributos adicionais são incluídos nos parâmetros criptográficos conforme o escopo escolhido (via flag `--scope` ou anotações no Secret de entrada): (1) **`strict` (padrão)**: inclui tanto o **`namespace`** quanto o **`name`** do segredo nos dados criptografados; se alguém alterar o nome ou o namespace no YAML do `SealedSecret`, o controlador recusará com `"decryption error"`; (2) **`namespace-wide`** (anotação `sealedsecrets.bitnami.com/namespace-wide: "true"`): vincula apenas o `namespace`, permitindo renomear livremente o segredo dentro daquele mesmo namespace; e (3) **`cluster-wide`** (anotação `sealedsecrets.bitnami.com/cluster-wide: "true"`): permite descriptografar o segredo em qualquer namespace e com qualquer nome.

## Exemplo
```bash
# Selar um segredo com escopo namespace-wide (permitindo renomeá-lo dentro do mesmo namespace, como em Kustomize hash suffix)
kubeseal --scope namespace-wide -o yaml < secret.yaml > sealed-secret.yaml
```

## Limites e trade-offs
Embora o modo padrão **`strict`** bloqueie alterações em `metadata.name` e `metadata.namespace`, o README oficial destaca que as chaves internas do mapa (`spec.encryptedData.<chave>`) **não** fazem parte do vínculo de nome/namespace e podem ser renomeadas livremente; já em fluxos que geram nomes de Secrets com sufixo de hash dinâmico (como o `secretGenerator` do Kustomize), o modo `strict` falhará ao renomear o Secret, exigindo `--scope namespace-wide`.

## Como verificar
Sele um segredo no modo padrão `strict`, edite manualmente `metadata.name` no arquivo `sealed-secret.yaml` gerado, aplique no cluster e verifique nos logs do controlador (`kubectl logs -n kube-system -l name=sealed-secrets-controller`) ou nos `Events` do `SealedSecret` o erro de descriptografia.

## Conexões
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Veja também: Bitnami Sealed Secrets: criptografia assimétrica de Secrets para GitOps (kubeseal e controlador SealedSecret).
- [[sealedsecrets-templates-metadados-ownerreferences-tipos-secret]] — Veja também: Bitnami Sealed Secrets: seção spec.template, labels/annotations do Secret gerado, funções Sprig e ownerReferences.
- [[sealedsecrets-certificado-publico-fetch-cert-offline-url]] — Referência cruzada direta com sealedsecrets-certificado-publico-fetch-cert-offline-url.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
