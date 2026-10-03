---
id: software.devops.tranche15.001440
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
fontes: ["https://raw.githubusercontent.com/lima-vm/lima/master/README.md", "https://lima-vm.io/docs/config/", "https://github.com/lima-vm/lima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lima: geração de SBOM CycloneDX em duas visões (`app` vs `mod`) para auditoria de cadeia de suprimentos

## Em uma frase
Desde a versão `v2.3`, os artefatos de release do Lima publicam um pacote de *Software Bill of Materials* (SBOM) no formato padrão CycloneDX contendo dois tipos distintos de inventário por binário: `*.bom.json` (`app`) e `bom.json` (`mod`).

## Por que importa
Ferramentas de segurança que escaneiam apenas o `go.mod` bruto costumam gerar falsos positivos por causa de dependências exclusivas de testes ou de outros sistemas operacionais que nunca entram no binário compilado final.

## Como funciona
O Lima resolve essa ambiguidade fornecendo ambas as visões: os arquivos SBOM gerados no modo `app` avaliam as *build constraints* e incluem estritamente os pacotes que o binário compilado realmente importa; já o SBOM no modo `mod` agrega todos os módulos declarados no módulo alvo (incluindo dependências de testes) para uma visão ampla do repositório.

## Exemplo
```bash
limactl --version
limactl info | jq .
```

## Limites e trade-offs
Ao auditar CVEs que afetam especificamente o binário em execução na estação de trabalho, priorize o arquivo `app` (`*.bom.json`) do sistema operacional e arquitetura correspondentes para evitar alertas de pacotes não compilados.

## Como verificar
Baixe o arquivo de SBOM da release oficial do Lima e compare a contagem de componentes entre o inventário `app` e o inventário `mod` com `jq '.components | length'`.

## Conexões
- [[lima-plain-mode-ssh-sudo-environment-variables-isolamento]] — Veja também: Lima: modo `plain`, variáveis de ambiente (`env`), política de `sudo` e endurecimento de acesso SSH.

## Fontes
- [Lima GitHub — README.md (Linux Virtual Machines, Automatic File Sharing & Port Forwarding, containerd/nerdctl/Docker/K8s Templates & CycloneDX SBOM)](https://raw.githubusercontent.com/lima-vm/lima/master/README.md) — README oficial do lima-vm/lima (CNCF Incubating) apresentando o fluxo limactl, templates de Docker e Kubernetes, geração de SBOM CycloneDX (app vs mod) e ecossistema de adotantes; consultado em 2026-10-03.
- [Lima Official Documentation — Configuration Guide (Default Spec, VM Types VZ/QEMU, Multi-Arch, Port Forwarding, Mounts & Plain Mode)](https://lima-vm.io/docs/config/) — Guia oficial de configuração do Lima detalhando a especificação padrão (4 vCPUs, 4 GiB RAM, 100 GiB disk), tipos de VM, montagens, redes, discos e modo plain; consultado em 2026-10-03.
- [Lima — Official GitHub Repository](https://github.com/lima-vm/lima) — Repositório oficial Apache-2.0 do Lima na CNCF; consultado em 2026-10-03.
