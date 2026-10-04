---
id: software.devops.tranche15.001446
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

# Colima: configuração declarativa (`colima.yaml`), precedência de diretórios `$COLIMA_HOME` e templates

## Em uma frase
Desde a versão `v0.4.0`, o Colima persiste todas as opções de cada instância em um arquivo YAML (`colima.yaml`), editável via `colima start --edit` e padronizável para novas instâncias via `colima template`.

## Por que importa
Evita repetir longas listas de flags na linha de comando e permite versionar a configuração padrão de rede, montagens, variáveis de ambiente e overrides do daemon Docker.

## Como funciona
Para localizar seus arquivos de configuração, o Colima segue uma ordem estrita de precedência quando `$COLIMA_HOME` não está definido: 1) `$HOME/.colima` (se existir); 2) `$XDG_CONFIG_HOME/colima` (se a variável estiver definida); 3) `~/.config/colima` (se existir); 4) `$HOME/.colima` no macOS. O editor padrão pode ser escolhido via `$EDITOR` ou `--editor code`.

## Exemplo
```bash
colima template --editor code
colima start --edit --editor code
```

## Limites e trade-offs
Alterações feitas com `colima template` afetam apenas novos perfis criados posteriormente; para modificar o perfil `default` já existente, deve-se usar `colima start --edit` ou editar `$COLIMA_HOME/default/colima.yaml`.

## Como verificar
Verifique o arquivo `$HOME/.colima/default/colima.yaml` e confirme que as alterações aplicadas permanecem ativas após reiniciar a instância.

## Conexões
- [[colima-dimensionamento-cpu-memory-disk-vz-rosetta-perfis]] — Veja também: Colima: dimensionamento de CPU, memória, expansão de disco, Rosetta 2 (`--vz-rosetta`) e múltiplos perfis.
- [[colima-customizacao-daemon-docker-containerd-registries-mirrors]] — Veja também: Colima: customização de `daemon.json` do Docker, `config.toml` do containerd e variáveis de ambiente na VM.

## Fontes
- [Colima GitHub — README.md (Docker, Containerd, Kubernetes & Incus Runtimes on macOS/Linux, GPU AI Workloads with krunkit & VM Customization)](https://raw.githubusercontent.com/abiosoft/colima/main/docs/FAQ.md) — README oficial do abiosoft/colima detalhando os runtimes suportados, compartilhamento de imagens com Kubernetes, execução de modelos de IA acelerados por GPU via krunkit e dimensionamento de VM; consultado em 2026-10-03.
- [Colima Official Documentation — docs/FAQ.md (COLIMA_HOME Precedence, colima.yaml Configuration, Docker/Containerd Overrides, Reachable IP & Provision Scripts)](https://raw.githubusercontent.com/abiosoft/colima/main/README.md) — FAQ técnico oficial do Colima cobrindo precedência de diretórios de configuração, customização de daemon.json, múltiplos perfis, endereço IP roteável e scripts de provisionamento; consultado em 2026-10-03.
- [Colima — Official GitHub Repository](https://github.com/abiosoft/colima) — Repositório oficial MIT do Colima; consultado em 2026-10-03.
