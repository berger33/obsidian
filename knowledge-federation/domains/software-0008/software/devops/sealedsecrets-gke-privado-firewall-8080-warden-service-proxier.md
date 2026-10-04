---
id: software.devops.tranche10.000929
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

# Bitnami Sealed Secrets: operação em clusters GKE privados (firewall 8080/8081) e restrições do GKE Warden (system:authenticated)

## Em uma frase
Conforme documenta o guia oficial `docs/GKE.md`, operar o Sealed Secrets no Google Kubernetes Engine (GKE) exige atenção a dois pontos: liberar a porta TCP `8080` no firewall do Control Plane para os nós em clusters GKE privados (ou usar selamento offline) e ajustar `rbac.serviceProxier` em clusters GKE `1.32.2+` onde o webhook **GKE Warden** proíbe bindings para `system:authenticated`.

## Por que importa
Em clusters GKE modernos (`1.32.2-gke.1182003` ou superior), instalar o Helm chart padrão do `sealed-secrets` falha imediatamente na admissão com o erro `GKE Warden rejected the request ... Binding any Role or ClusterRole to Group "system:authenticated" is forbidden`. O documento oficial `docs/GKE.md` explica a causa exata e as duas soluções suportadas.

## Como funciona
(1) **Private GKE Clusters**: como um firewall bloqueia por padrão o Control Plane do GKE de falar diretamente com a porta `8080` do container do controlador nos nós workers, `kubeseal --fetch-cert` via API proxy falha a menos que você crie uma regra de firewall liberando `tcp:8080` (e `tcp:8081` para métricas) a partir do `masterIpv4CidrBlock` ou utilize selamento offline (`kubeseal --cert=cert.pem`); e (2) **GKE Warden Restrictions (`1.32.2+`)**: por padrão, o chart cria a Role `service-proxier` vinculada ao grupo amplo `system:authenticated` para permitir o `--fetch-cert`. No GKE moderno, o administrador deve sobrescrever o `values.yaml` do Helm chart com **`rbac.serviceProxier.create: false`** (Opção 1, mais simples) ou vincular `rbac.serviceProxier.subjects` a um Google Group restrito da organização (Opção 2).

## Exemplo
```yaml
# Configuração values.yaml do Helm chart sealed-secrets recomendada em docs/GKE.md para compatibilidade com o GKE Warden (1.32.2+)
rbac:
  serviceProxier:
    create: false
```

## Limites e trade-offs
Ao desabilitar o `serviceProxier` (`rbac.serviceProxier.create: false`), usuários sem permissão de administrador não poderão usar `kubeseal` buscando o certificado dinamicamente via proxy do API Server; combine essa opção com a distribuição do certificado público (`kubeseal --cert <url-ou-arquivo>`) para os desenvolvedores.

## Como verificar
Em um cluster GKE `1.32+`, instale o Helm chart passando `--set rbac.serviceProxier.create=false` e confirme que o webhook `warden-validating.common-webhooks.networking.gke.io` aceita todos os recursos RBAC.

## Conexões
- [[sealedsecrets-backup-chaves-privadas-recovery-offline-unseal]] — Veja também: Bitnami Sealed Secrets: backup das chaves privadas de selamento, Disaster Recovery e descriptografia offline (--recovery-unseal).
- [[sealedsecrets-instalacao-ambientes-restritos-norbac-namespaces]] — Veja também: Bitnami Sealed Secrets: instalação em ambientes restritos sem RBAC (controller-norbac.yaml) e escopo de namespaces.
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-certificado-publico-fetch-cert-offline-url]] — Referência cruzada direta com sealedsecrets-certificado-publico-fetch-cert-offline-url.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
