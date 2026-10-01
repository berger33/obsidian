# Merge completo — Knowledge Federation

Data: 2026-10-01

## Entrega principal

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

Checksum:

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz.sha256
```

SHA-256:

```text
20b13859724d5beb04142e6a175d25284d9dc236fd4ee9b795a918fccbaabac6
```

## O que foi mesclado

O arquivo contém o merge lógico completo dos materiais materializados até agora:

```text
MERGE-COMPLETO/00-vault-consolidado/
MERGE-COMPLETO/10-lotes/
MERGE-COMPLETO/90-ledger/
MERGE-COMPLETO/99-relatorios/
```

Inclui:

- vault consolidado curado com 7.100 notas;
- 33 pacotes sequenciais de lotes, expandidos dentro do TAR;
- lotes 001 a 3300;
- 660.000 notas sequenciais materializadas;
- checkpoint ledger `ledger-v1000000-mat8000.zip` dentro de `90-ledger/`;
- relatórios, manifestos e índices.

## Totais representados

```text
Vault curado: 7.100 notas
Lotes sequenciais: 3.300
Notas sequenciais: 660.000
Total materializado representado: 667.100 notas
Entradas no TAR: 670.669
Conteúdo operacional regulado: 0
```

## Integridade

Validações executadas:

```text
xz -t archives/merge-completo-materializado-1m.tar.xz
```

Resultado: OK.

Também foi listado o TAR antes da poda dos zips individuais:

```text
tar_entries=670669
```

## Por que os zips sequenciais foram removidos depois?

Depois do merge validado, os zips sequenciais individuais foram podados para reduzir o workspace de aproximadamente 994M para aproximadamente 276M.

Registro da poda:

```text
knowledge-federation/archives/pruned-after-merge/sequential-zips-pruned.txt
```

Os conteúdos desses zips estão preservados dentro do merge completo em:

```text
MERGE-COMPLETO/10-lotes/
```

## Como extrair

```bash
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```

## Como abrir no Obsidian

Após extrair, abra uma destas pastas como vault:

```text
MERGE-COMPLETO/00-vault-consolidado/study-vault-1m-packs/
```

Ou abra um intervalo específico de lotes em:

```text
MERGE-COMPLETO/10-lotes/0001-0100/
MERGE-COMPLETO/10-lotes/0101-0200/
...
MERGE-COMPLETO/10-lotes/3201-3300/
```

Cada intervalo contém `00-Inicio/Home.md`, MOCs, Canvas e notas.

## Segurança

Conteúdos de cannabis medicinal e micologia permanecem educacionais, documentais e não operacionais. O material usa `conteudo_operacional: false` e aviso de domínio regulado para orientar uso seguro: estudo, rastreabilidade, documentação e perguntas para profissionais habilitados.
