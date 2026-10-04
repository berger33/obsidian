---
id: software.devops.tranche15.001448
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

# Colima: endereço IP roteável da VM (`--network-address`), autostart em background e recuperação de espaço em disco

## Em uma frase
O Colima suporta a atribuição de um endereço IP dedicado e diretamente alcançável a partir do host (`--network-address`), inicialização automática em segundo plano (`--foreground` com `brew services`) e limpeza de espaço em disco.

## Por que importa
Embora o port-forwarding em `localhost` atenda à maioria dos containers, cenários como acessar instâncias Incus diretamente por IP, testar NodePorts ou expor serviços sem colisão de portas locais exigem que a VM possua um IP roteável pelo macOS.

## Como funciona
Ao iniciar com `colima start --network-address` (ou `network.address: true` no YAML), o Colima configura uma interface de rede dedicada cujo IP aparece em `colima list`. Já para executar o Colima automaticamente no login do macOS, utiliza-se `brew services start colima` (que emprega `colima start --foreground`).

## Exemplo
```bash
colima start --network-address
colima list
brew services list
```

## Limites e trade-offs
Caminhos de montagem no host que contenham espaços em branco no nome do diretório não são suportados nos bind mounts do Colima e podem causar falhas de montagem ou diretórios vazios.

## Como verificar
Execute `colima list` e teste `ping -c 1 <ADDRESS>` contra o endereço IP exibido na coluna `ADDRESS`.

## Conexões
- [[colima-customizacao-daemon-docker-containerd-registries-mirrors]] — Veja também: Colima: customização de `daemon.json` do Docker, `config.toml` do containerd e variáveis de ambiente na VM.
- [[colima-lima-overrides-provision-scripts-atualizacao-runtime]] — Veja também: Colima: scripts de provisionamento customizados (`provision`), overrides do Lima e atualização de runtimes.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
