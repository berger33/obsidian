---
id: software.seguranca.tranche12.001124
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

# Bibliotecas de Ameaças do Caldera: Plugins **`stockpile`**, **`atomic`** e **`emu`** (Planos Oficiais do **MITRE CTID** — FIN6, APT29, Sandworm, LockBit)

## Em uma frase
Ao instalar o Caldera, de onde vêm as centenas de técnicas e perfis de grupos criminosos prontos para uso? Eles vêm de três plugins oficiais mantidos pela MITRE que funcionam como arsenais modulares de TTPs:

## Por que importa
Primeiro, o plugin **`stockpile`** (`mitre/stockpile`), que é o armazém padrão de *Abilities*, *Adversary Profiles*, *Planners* e *Obfuscators* criados pela equipe do Caldera; segundo, o plugin **`atomic`** (`mitre/atomic`), que integra toda a biblioteca do **Red Canary Atomic Red Team** diretamente dentro do Caldera; e terceiro, o plugin **`emu`** (`mitre/emu`), que importa os planos completos de emulação de adversários do **MITRE Center for Threat-Informed Defense (CTID Adversary Emulation Library)**!

## Como funciona
Com o plugin **`emu`** ativo, sua equipe pode executar com poucos cliques planos de emulação baseados em inteligência real de ameaças para grupos como **APT29 (Cozy Bear)**, **FIN6**, **FIN7**, **menuPass**, **Sandworm**, **OilRig**, **Wizard Spider** e **Turla**!

## Exemplo
```bash
# Verificar no arquivo de configuracao conf/default.yml quais plugins de arsenal (stockpile, atomic, emu) estao habilitados no Caldera
grep -A 15 "^plugins:" ./caldera/conf/default.yml
ls -la ./caldera/plugins/stockpile/data/adversaries/
```

## Limites e trade-offs
Para organizações que possuem sistemas industriais (**ICS / SCADA / OT**) ou sistemas de **Inteligência Artificial / Machine Learning**, o ecossistema do Caldera oferece ainda os plugins especializados **`caldera-ot`** (`mitre/caldera-ot` para protocolos Modbus, DNP3, BACnet e OPC UA mapeados ao MITRE ATT&CK for ICS) e **`arsenal`** (`mitre-atlas/arsenal` mapeado ao **MITRE ATLAS**)!

## Como verificar
Mantenha os submódulos dos plugins `stockpile`, `emu` e `atomic` atualizados no seu ambiente de homologação para incorporar novos perfis de ameaças publicados pelo CTID.

## Conexões
- [[caldera-abilities-adversary-profiles-planners-facts-parsers]] — Veja também: Motor de Decisão Autônoma do Caldera: **Abilities**, **Adversary Profiles**, **Planners (`atomic`, `batch`, `buckets`)**, **Facts** e **Parsers**.
- [[caldera-furtividade-ofuscadores-jitter-builder-evasao-edr]] — Veja também: Controles de Furtividade (*Stealth*) em Operações do Caldera: **Obfuscators** (`plain-text`, `base64`, `caesar`, `steganography`), **Jitter** e **Autonomous Mode**.
- [[caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins]] — Referência cruzada direta com caldera-arquitetura-plataforma-emulacao-adversarios-c2-plugins.
- [[atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator]] — Referência cruzada direta com atomicredteam-integracao-mitre-caldera-vectr-cobertura-attack-navigator.

## Fontes
- [MITRE Caldera Official GitHub — Automated Adversary Emulation, Red Team & Incident Response Platform](https://raw.githubusercontent.com/mitre/caldera/master/README.md) — repositório oficial do MITRE Caldera v5 cobrindo o Core C2 Server, interface VueJS Magma e ecossistema de plugins (`sandcat`, `stockpile`, `atomic`, `emu`, `debrief`, `response`); consultado em 2026-10-03.
- [MITRE Caldera Official Documentation — Learning the Terminology (`Agents`, `Abilities`, `Adversaries`, `Operations`, `Planners`, `Facts`, `Parsers`)](https://caldera.readthedocs.io/en/latest/Learning-the-terminology.html) — documentação oficial ReadTheDocs detalhando a arquitetura de planejamento orientado a fatos e agentes do Caldera; consultado em 2026-10-03.
