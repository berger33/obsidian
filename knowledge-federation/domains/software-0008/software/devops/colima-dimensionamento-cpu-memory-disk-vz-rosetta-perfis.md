---
id: software.devops.tranche15.001445
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
fontes: ["https://raw.githubusercontent.com/abiosoft/colima/main/README.md", "https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md", "https://github.com/abiosoft/colima"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Colima: dimensionamento de CPU, memória, expansão de disco, Rosetta 2 (`--vz-rosetta`) e múltiplos perfis

## Em uma frase
O Colima permite customizar os recursos de hardware da VM (`--cpu`, `--memory`, `--disk`), ativar o hipervisor nativo do macOS com Rosetta 2 (`--vm-type=vz --vz-rosetta`) e operar múltiplas instâncias isoladas via perfis (`--profile` ou `-p`).

## Por que importa
Desenvolvedores frequentemente precisam de uma instância leve para o dia a dia e de um segundo perfil mais robusto com Kubernetes ou maior RAM para testes de integração, além de emulação rápida `amd64` em Apple Silicon.

## Como funciona
Para alterar CPU ou memória de uma instância existente, basta executar `colima stop` seguido de `colima start --cpu 4 --memory 8`. O tamanho do disco (`--disk`) também pode ser expandido após a criação da VM. Para criar uma instância separada, usa-se `colima start --profile k8s-lab --kubernetes`.

## Exemplo
```bash
colima stop
colima start --cpu 4 --memory 8 --disk 120 --vm-type=vz --vz-rosetta
colima list
```

## Limites e trade-offs
O tamanho do disco virtual pode ser aumentado após a criação da VM, mas não pode ser reduzido in-place sem recriar a instância (`colima delete`).

## Como verificar
Execute `colima list` para conferir os valores atualizados de `CPUS`, `MEMORY`, `DISK` e `ARCH` da instância em execução.

## Conexões
- [[colima-ai-workloads-gpu-krunkit-docker-model-runner-ramalama]] — Veja também: Colima: aceleração por GPU para modelos de IA (`--vm-type krunkit`) com Docker Model Runner e Ramalama.
- [[colima-configuracao-yaml-colima-home-xdg-template-editor]] — Veja também: Colima: configuração declarativa (`colima.yaml`), precedência de diretórios `$COLIMA_HOME` e templates.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
