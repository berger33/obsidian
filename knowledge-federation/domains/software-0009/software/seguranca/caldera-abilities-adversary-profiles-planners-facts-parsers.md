---
id: software.seguranca.tranche12.001123
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/mitre/caldera/master/README.md", "https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Motor de Decisão Autônoma do Caldera: **Abilities**, **Adversary Profiles**, **Planners (`atomic`, `batch`, `buckets`)**, **Facts** e **Parsers**

## Em uma frase
O que torna o **MITRE Caldera** radicalmente diferente de um simples agendador de scripts é o seu **sistema de planejamento orientado a fatos (*Fact-Driven Planning*)**, que permite que uma operação descubra informações em um passo e as utilize automaticamente nos passos seguintes!

## Por que importa
Na terminologia do Caldera: uma **`Ability`** é a implementação de uma técnica/subtécnica ATT&CK (contendo o comando, plataforma/executor, payloads e um **`parser`**); um **`Adversary Profile`** agrupa as *Abilities* de um ator de ameaça; uma **`Operation`** executa um *Adversary Profile* contra um grupo de agentes sob a regência de um **`Planner`** (`atomic` em ordem sequencial, `batch` tudo de uma vez, ou `buckets` agrupado por tática ATT&CK)!

## Como funciona
A mágica acontece no ciclo **Link -> Output -> Parser -> Fact -> Requirement**: quando um agente executa um `link` (ex.: listar arquivos sensíveis) e devolve o `stdout`, o **`parser`** do Caldera extrai variáveis identificáveis chamadas **`Facts`** (ex.: `host.file.path = /home/app/secret.doc`); a próxima `Ability` da cadeia (que referencia `#{host.file.path}` e exige que esse *fact* exista via *fact requirements*) é então instanciada automaticamente para comprimir e exfiltrar aquele arquivo exato!

## Exemplo
```yaml
# Exemplo de Ability YAML do Caldera que requer o fact 'host.dir.staged' e usa-o dinamicamente no comando
- id: 90c2efaa-8205-480d-8b6a-1a2b3c4d5e6f
  name: Compress Staged Directory
  description: Comprime o diretorio de staging descoberto anteriormente na operacao
  tactic: collection
  technique:
    attack_id: T1560.001
    name: "Archive Collected Data: Archive via Utility"
  platforms:
    linux:
      sh:
        command: |
          tar -czf /tmp/exfil_bundle.tar.gz #{host.dir.staged}
        cleanup: |
          rm -f /tmp/exfil_bundle.tar.gz
```

## Limites e trade-offs
Graças a esse grafo de **Facts e Requirements**, você pode rodar o mesmo *Adversary Profile* em 20 servidores completamente diferentes: em cada servidor, o Caldera descobrirá os usuários, processos e arquivos locais reais daquela máquina e adaptará os comandos subsequentes automaticamente!

## Como verificar
Você também pode pré-carregar uma **`Fact Source`** inicial na operação (por exemplo, credenciais ou faixas de IP de laboratório conhecidas) para acelerar testes de movimentação lateral.

## Conexões
- [[caldera-agentes-sandcat-manx-ragdoll-c2-contacts-paw]] — Veja também: Agentes do Caldera (**`Sandcat`**, **`Manx`** e **`Ragdoll`**): Identificadores **`paw`**, Canais de Contato C2 (**HTTP, TCP, DNS, Gist**) e Grupos Red/Blue.
- [[caldera-plugins-stockpile-emu-atomic-planos-ctid]] — Veja também: Bibliotecas de Ameaças do Caldera: Plugins **`stockpile`**, **`atomic`** e **`emu`** (Planos Oficiais do **MITRE CTID** — FIN6, APT29, Sandworm, LockBit).
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
