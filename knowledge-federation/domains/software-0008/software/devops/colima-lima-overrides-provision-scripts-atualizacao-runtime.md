---
id: software.devops.tranche15.001449
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: scripts de provisionamento customizados (`provision`), overrides do Lima e atualização de runtimes

## Em uma frase
O `colima.yaml` suporta blocos de provisionamento (`provision:`) executados como `system` (`root`) ou `user` durante a inicialização da VM, além de comandos nativos para atualizar o runtime de containers sem destruir os dados.

## Por que importa
Permite instalar pacotes extras na VM (como certificados corporativos, utilitários de rede ou módulos de kernel) e manter a versão do Docker ou containerd atualizada mesmo entre releases do Colima.

## Como funciona
Scripts definidos em `provision:` com `mode: system` ou `mode: user` são repassados à camada subjacente do Lima e executados a cada start. Além disso, o usuário pode acessar a VM via `colima ssh` para diagnóstico ou atualizar a versão do runtime em execução.

## Exemplo
```yaml
provision:
  - mode: system
    script: |
      apk add --no-cache curl jq || apt-get update && apt-get install -y curl jq
```

## Limites e trade-offs
Scripts de provisionamento devem ser escritos de forma idempotente, pois são reexecutados quando a máquina virtual é iniciada.

## Como verificar
Execute `colima ssh -- which jq` após iniciar a instância para verificar que o script de provisionamento instalou os pacotes esperados.

## Conexões
- [[colima-rede-network-address-ip-alcancavel-port-forwarding]] — Veja também: Colima: endereço IP roteável da VM (`--network-address`), autostart em background e recuperação de espaço em disco.
- [[colima-comparacao-lima-minikube-kind-k3d-troubleshooting]] — Veja também: Colima: comparação arquitetural com Lima, Minikube, kind e k3d e resolução de problemas comuns.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
