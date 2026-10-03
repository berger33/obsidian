---
id: software.devops.tranche15.001447
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

# Colima: customização de `daemon.json` do Docker, `config.toml` do containerd e variáveis de ambiente na VM

## Em uma frase
O arquivo `colima.yaml` permite injetar configurações nativas diretamente no `daemon.json` do Docker (sob a chave `docker:`), customizar o containerd por perfil e propagar variáveis de ambiente (`env:`) do host para dentro da VM.

## Por que importa
Em redes corporativas que exigem proxies HTTP, espelhos de registry (`registry-mirrors`), registros internos sem TLS (`insecure-registries`) ou certificados CA privados, configurar essas opções diretamente no `colima.yaml` garante que elas sobrevivam a reinicializações da VM.

## Como funciona
Ao definir o bloco `docker:` no `colima.yaml` (ou passar `--env MY_VAR=valor` em `colima start`), o Colima gera a configuração interna da máquina virtual durante o boot e reinicia o serviço do runtime com os parâmetros aplicados.

## Exemplo
```yaml
cpu: 4
memory: 8
env:
  HTTPS_PROXY: "http://proxy.corp.internal:3128"
docker:
  insecure-registries:
    - "registry.corp.internal:5000"
  registry-mirrors:
    - "https://mirror.gcr.io"
```

## Limites e trade-offs
Editar manualmente `/etc/docker/daemon.json` diretamente via `colima ssh` sem registrar a mudança na seção `docker:` do `colima.yaml` fará com que a customização seja sobrescrita no próximo ciclo de `colima start`.

## Como verificar
Após reiniciar o Colima, execute `docker info` no host e confirme que os `Insecure Registries` e `Registry Mirrors` listados refletem o `colima.yaml`.

## Conexões
- [[colima-configuracao-yaml-colima-home-xdg-template-editor]] — Veja também: Colima: configuração declarativa (`colima.yaml`), precedência de diretórios `$COLIMA_HOME` e templates.
- [[colima-rede-network-address-ip-alcancavel-port-forwarding]] — Veja também: Colima: endereço IP roteável da VM (`--network-address`), autostart em background e recuperação de espaço em disco.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
