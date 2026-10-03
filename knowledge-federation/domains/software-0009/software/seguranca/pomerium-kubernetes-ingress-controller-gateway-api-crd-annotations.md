---
id: software.seguranca.tranche03.000246
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://www.pomerium.com/docs", "https://raw.githubusercontent.com/pomerium/pomerium/main/README.md", "https://github.com/pomerium/pomerium"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Pomerium Kubernetes Ingress Controller e Gateway API: definição declarativa de rotas e políticas via `Ingress` Annotations e CRDs

## Em uma frase
Em clusters Kubernetes, o **Pomerium Ingress Controller** permite declarar rotas Zero-Trust e políticas de autorização PPL diretamente nos objetos nativos **`Ingress`** do Kubernetes (`ingressClassName: pomerium` + anotações `ingress.pomerium.io/*`) ou recursos da **Kubernetes Gateway API**!

## Por que importa
Manter um arquivo `config.yaml` monolítico separado dos manifests Kubernetes de cada microsserviço obriga uma equipe central a editar a configuração do proxy toda vez que uma squad cria um novo serviço interno.

## Como funciona
Com o Pomerium Ingress Controller, a própria squad declara o `Ingress` do seu serviço no repositório GitOps com a anotação **`ingress.pomerium.io/policy`** (em YAML PPL), e o controlador sincroniza automaticamente a rota e a política com o `Databroker` do Pomerium em tempo real!

## Exemplo
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: prometheus-internal-ui
  namespace: monitoring
  annotations:
    ingress.pomerium.io/pass_identity_headers: "true"
    ingress.pomerium.io/policy: |
      - allow:
          and:
            - domain:
                is: internal.corp
            - claim/groups:
                has: observability-readers
spec:
  ingressClassName: pomerium
  tls:
    - hosts:
        - prometheus.internal.corp
      secretName: prometheus-tls
  rules:
    - host: prometheus.internal.corp
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: prometheus-server
                port:
                  number: 9090
```

## Limites e trade-offs
Para proteger a comunicação entre o Pomerium Proxy e o Pod de destino dentro do cluster, use a anotação `ingress.pomerium.io/secure_upstream: "true"` quando o Pod backend já servir HTTPS.

## Como verificar
Verifique o status de reconciliação do objeto Ingress executando `kubectl describe ingress prometheus-internal-ui -n monitoring`.

## Conexões
- [[pomerium-acesso-tcp-ssh-rdp-postgres-tunelamento-autenticado]] — Veja também: Pomerium Rotas `TCP` (`tcp+https://`): acesso Zero-Trust a bancos de dados (`PostgreSQL`, `Redis`), `SSH` e `RDP` sem VPN.
- [[pomerium-arquitetura-distribuida-authenticate-authorize-proxy-databroker]] — Veja também: Pomerium Arquitetura de Serviços Distribuídos (`Authenticate`, `Authorize`, `Proxy` e `Databroker`): isolamento e escalabilidade.

## Fontes
- [Pomerium Official Documentation — What is Pomerium? (BeyondCorp Zero-Trust Access Proxy, Authenticate/Authorize/Proxy Flow & Core Architecture)](https://www.pomerium.com/docs) — Documentação oficial do Pomerium explicando o modelo de acesso sem cliente baseado em identidade, dispositivo e contexto por requisição; consultado em 2026-10-03.
- [Pomerium GitHub — README.md (Identity and Context-Aware Reverse Proxy, Clientless Access & Continuous Verification)](https://raw.githubusercontent.com/pomerium/pomerium/main/README.md) — README oficial do pomerium/pomerium apresentando a arquitetura do proxy reverso Zero-Trust em Go e Envoy; consultado em 2026-10-03.
- [Pomerium — Official GitHub Repository](https://github.com/pomerium/pomerium) — Repositório oficial Apache-2.0 do Pomerium; consultado em 2026-10-03.
